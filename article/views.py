from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.views import APIView


from article.models import Article, Comment
from article.serializers import (ArticleSerializer,
                                 ArticleActionSerializer,
                                 ArticleCreateSerializer,
                                 ArticlePagination, CommentCreateSerializer, CommentSerializer)


def home_view(request):
    return render(request, 'index.html')


class ArticleListApiView(ListAPIView):
    queryset = Article.objects.all()
    pagination_class = ArticlePagination
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'user__username']


@api_view(['GET'])
def articles_list_view(request, *args, **kwargs):
    queryset = Article.objects.all()
    paginate = ArticlePagination()
    uid = request.GET.get('uid')
    search = request.GET.get('search')
    if uid is not None:
        queryset2 = queryset.filter(user__id=uid)
        page_obj = paginate.paginate_queryset(queryset2, request)
        serializer = ArticleSerializer(page_obj, many=True)
        return paginate.get_paginated_response(serializer.data)
    if search is not None:
        queryset2 = queryset.filter(Q(user__username__icontains=search) | Q(content__icontains=search))
        page_obj = paginate.paginate_queryset(queryset2, request)
        serializer = ArticleSerializer(page_obj, many=True)
        return paginate.get_paginated_response(serializer.data)
    page_obj = paginate.paginate_queryset(queryset, request)
    serializer = ArticleSerializer(page_obj, many=True)
    return paginate.get_paginated_response(serializer.data)


@api_view(['GET'])
def articles_detail_view(request, article_id, *args, **kwargs):
    queryset = Article.objects.filter(id=article_id)
    if not queryset.exists():
        return Response({}, status=404)
    serializer = ArticleSerializer(queryset.first())
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def articles_create_view(request, *args, **kwargs):
    serializer = ArticleCreateSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        aid = serializer.data.get('id')
        serializer = ArticleSerializer(Article.objects.get(pk=aid))
        return Response(serializer.data, status=201)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def articles_delete_view(request, article_id, *args, **kwargs):
    qs = Article.objects.filter(id=article_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({'msg': 'you are not able to delete it'}, status=403)
    obj = qs.first()
    obj.delete()
    return Response({'msg': 'Blog removed'}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def articles_action_view(request, *args, **kwargs):
    msg = {}
    serializer = ArticleActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        article_id = data.get('id')
        action = data.get('action')
        content = data.get('content') if data.get('content') else ""
        qs = Article.objects.filter(id=article_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if action == "unlike":
            obj.likes.remove(request.user)
            serializer = ArticleSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "like":
            obj.likes.add(request.user)
            serializer = ArticleSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "retweet":
            new_tweet = Article.objects.create(user=request.user, parent=obj, content=content)
            serializer = ArticleSerializer(new_tweet)
            return Response(serializer.data, status=200)
            # TODO 转发
        msg = action + " success"
    return Response({'msg': msg}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create_view(request, *args, **kwargs):
    aid = request.POST.get('aid')
    article = Article.objects.filter(pk=aid).first()
    if not article:
        return Response({'msg': 'article does not exist'}, status=404)
    serializer = CommentCreateSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        aid = serializer.data.get('id')
        serializer = CommentSerializer(Comment.objects.get(pk=aid))
        return Response(serializer.data, status=201)
