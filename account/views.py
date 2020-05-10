from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.forms import UserRegisterForm, UserLoginForm
from account.models import User
from userprofile.models import UserProfile
from userprofile.serializers import UserProfileSerializer


@api_view(['POST'])
def user_login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.update_or_create(user=user)
        token = Token.objects.get(user=user)
        profile = UserProfile.objects.filter(user=user).first()
        return Response({'token': token.key,
                         'user': UserProfileSerializer(profile).data},
                        status=200)
    return Response({'msg': 'login failed'}, status=401)


@api_view(['POST'])
def user_register(request):
    rform = UserRegisterForm(request.POST)
    if rform.is_valid():
        username = rform.cleaned_data.get('username')
        email = rform.cleaned_data.get('email')
        password = rform.cleaned_data.get('password')
        if not User.objects.filter(
                Q(username=username) | Q(email=email)).exists():
            password = make_password(password)
            user = User.objects.create(username=username, email=email,
                                       password=password)
            if user:
                return Response({'msg': '注册成功', 'code': 1}, status=200)
        else:
            return Response({'msg': '用户已存在', 'code': -1}, status=200)
    return Response({'msg': '注册失败', 'code': -2}, status=200)


def user_logout(request):
    request.sess.flush()
    return redirect(reverse('home'))


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_change_password(request, *args, **kwargs):
    username = request.user
    old_password = request.POST.get('old_password', None)
    new_password = request.POST.get('new_password', None)
    user = authenticate(username=username, password=old_password)
    if user and new_password:
        password = make_password(new_password)
        User.objects.filter(pk=user.pk).update(password=password)
        return Response({'msg': 'change password success'}, status=201)
    else:
        return Response({'msg': 'invalid user or password'}, status=403)
