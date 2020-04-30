from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.forms import UserRegisterForm, UserLoginForm
from account.models import UserProfile
from account.serializers import UserDetailSerializer


@api_view(['POST'])
def user_login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user:
        token = Token.objects.update_or_create(user=user)
        token = Token.objects.get(user=user)
        return Response({'token': token.key,
                         'user': UserDetailSerializer(user, context={'request': request}).data}, status=200)
    return Response({'msg': 'login failed'}, status=401)

@api_view(['POST'])
def user_register(request):
    rform = UserRegisterForm(request.POST)
    if rform.is_valid():
        username = rform.cleaned_data.get('username')
        email = rform.cleaned_data.get('email')
        phone_number = rform.cleaned_data.get('phone_number')
        password = rform.cleaned_data.get('password')
        if not UserProfile.objects.filter(
                Q(username=username) | Q(email=email) | Q(phone_number=phone_number)).exists():
            password = make_password(password)
            user = UserProfile.objects.create(username=username, phone_number=phone_number, email=email,
                                                password=password)
            if user:
                return Response({'msg': '注册成功','code':1},status=200)
        else:
            return Response({'msg': '用户已存在','code':-1},status=200)
    return Response({'msg': '注册失败','code':-2},status=200)


def user_logout(request):
    request.sess.flush()
    return redirect(reverse('home'))


@api_view(['GET'])
def user_detail(request):
    username = request.GET.get('username')
    if not username:
        return Response({'msg':'User does not exist'},status=404)
    qs = UserProfile.objects.filter(username=username).first()
    if not qs:
        return Response({'msg':'User does not exist'},status=404)
    serializer = UserDetailSerializer(qs)
    return Response(serializer.data,status=200)    
    


def user_center(request):
    return HttpResponse('个人中心')

