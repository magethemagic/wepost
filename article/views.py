from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from article.models import Article
from article.serializers import (ArticleSerializer, 
                                ArticleActionSerializer, 
                                ArticleCreateSerializer,
                                ArticlePaginations)


def home_view(request):
    articles = Article.objects.all()
    return render(request, 'pages/home.html', context={'articles': articles}, status=200)


@api_view(['GET'])
def articles_list_view(request, *args, **kwargs):
    queryset = Article.objects.all()
    paginate = ArticlePaginations()
    page_obj = paginate.paginate_queryset(queryset,request)
    serializer = ArticleSerializer(page_obj, many=True)
    return Response(serializer.data, status=200)


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
            new_tweet = Article.objects.create(user=request.user, parent=obj,content=content)
            serializer = ArticleSerializer(new_tweet)
            return Response(serializer.data, status=200)
            # TODO 转发
        msg = action + " success"
    return Response({'msg': msg}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create_view(request, *args, **kwargs):
    pass