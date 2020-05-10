from django.urls import path

from .views import (user_login,
                    user_logout,
                    user_register, user_change_password)

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('changepwd/', user_change_password, name='changepwd')
]
