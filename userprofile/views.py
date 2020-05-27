from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import User
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer, UserProfileUpdateSerializer


@api_view(['GET'])
def user_detail_uid_view(request, uid, *args, **kwargs):
    qs = UserProfile.objects.filter(user__id=uid)
    if not qs.exists():
        return Response({'msg': 'user does not exists'}, status=404)
    serializer = UserProfileSerializer(qs.first())
    return Response(serializer.data, status=200)


@api_view(['GET'])
def user_detail_view(request, *args, **kwargs):
    username = request.GET.get('username')
    if not username:
        return Response({'msg': 'User does not exist'}, status=404)
    qs = UserProfile.objects.filter(user__username__iexact=username).first()
    if not qs:
        return Response({'msg': 'User does not exist'}, status=404)
    serializer = UserProfileSerializer(qs)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_follow_view(request, uid, *args, **kwargs):
    me = request.user
    to_followed = User.objects.filter(pk=uid)
    action = request.data.get('action') or ''
    context = {}
    if me.id == uid:
        context['followers_count'] = me.userprofile.followers.count()
        return Response(context, status=200)
    if not to_followed.exists():
        return Response({}, status=404)
    other = to_followed.first()
    profile = other.userprofile
    if action == 'unfollow':
        context['msg'] = 'removed'
        profile.followers.remove(me)
    elif action == 'follow':
        context['msg'] = 'added'
        profile.followers.add(me)
    else:
        pass
    context['followers_count'] = profile.followers.count()
    return Response(context, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_is_follower(request, uid):
    user = request.user
    if user.id == uid:
        return Response({'msg': 'self'}, status=200)
    else:
        profile = User.objects.filter(pk=uid).first().userprofile
        print(profile.followers.all(), user)
        if user in profile.followers.all():
            return Response({'code': 1}, status=200)
        else:
            return Response({'code': -1}, status=200)


@api_view(['GET'])
def get_familiar_user(request, uid, *args, **kwargs):
    userquery = User.objects.filter(pk=uid).first()
    familiar_user = userquery.userprofile.followers.count()
    print(familiar_user)
    serializer = UserProfileSerializer(familiar_user, many=True)
    return Response(serializer.data, status=200)


class ChangProfileView(UpdateAPIView):
    serializer_class = UserProfileUpdateSerializer
    queryset = UserProfile.objects.all()

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user.userprofile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)
