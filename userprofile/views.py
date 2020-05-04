from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.models import User
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer


@api_view(['GET'])
def user_detail_username_view(request, username, *args, **kwargs):
    qs = UserProfile.objects.filter(user__username__iexact=username)
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
def user_follow_view(request, username, *args, **kwargs):
    me = request.user
    to_followed = User.objects.filter(username=username)
    action = request.data.get('action') or ''
    context = {}
    if me.username == username:
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
