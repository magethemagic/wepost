import random

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect, render
# Create your views here.
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from TwitterDjango.settings import EMAIL_FROM
from account.forms import UserRegisterForm
from account.models import User, EmailValidateModel
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


def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def send_email(email, send_type='register'):
    code = generate_random_str(4)
    if send_type == 'register':
        email_title = 'WePost注册链接'
        email_body = '请点击下面的连接激活你的账号: http://127.0.0.1:8080/user/register/{0}'.format(code)
    else:
        email_title = 'WePost重置密码链接'
        email_body = '请点击下面的连接修改你的密码: http://127.0.0.1:8080/user/resetpwd?code={0}'.format(code)

    send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
    # 如果成功保存到数据库
    if send_status:
        model = EmailValidateModel.objects.update_or_create(
            email=email,
            validate_code=code,
            send_type=send_type
        )
        model.save()
    return send_status


@api_view(['POST'])
def send_reset_email(request):
    email = request.POST.get('email')
    info = send_email(email, 'forgetpwd')
    if info:
        return Response({'msg': 'success', 'code': 1}, status=200)
    else:
        return Response({'msg': 'failed', 'code': -1}, status=200)


@api_view(['POST'])
def reset_password_2(request):
    context = {}
    code = request.POST.get('code')
    print(code)
    if not code:
        context['msg'] = 'no validate code error'
        context['code'] = -1
        return Response(context, status=200)
    email = EmailValidateModel.objects.filter(validate_code=code)
    if not email:
        context['msg'] = 'email does not exist'
        context['code'] = -2
        return Response(context, status=200)
    email_ = email.first()
    user = User.objects.filter(email=email_.email)
    if not user:
        context['msg'] = 'user does not exist'
        context['code'] = -2
        return Response(context, status=200)
    dest_user = user.first()
    password = request.POST.get('password')
    if not password:
        context['msg'] = 'password does not exist'
        context['code'] = -3
        return Response(context, status=200)
    password_ = make_password(password)
    dest_user.password = password_
    dest_user.save()
    Token.objects.update_or_create(user=dest_user)
    email_.delete()
    context['msg'] = 'reset success'
    context['code'] = 1
    return Response(context, status=200)
