from django.urls import path
from .views import user_detail_username_view, user_detail_view, user_follow_view

urlpatterns = [
    path('<str:username>', user_detail_username_view),
    path('', user_detail_view),
    path('<str:username>/follow', user_follow_view)
]
