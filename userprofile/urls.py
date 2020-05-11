from django.urls import path
from .views import user_detail_uid_view, user_detail_view, user_follow_view, get_is_follower, ChangProfileView

urlpatterns = [
    path('<int:uid>', user_detail_uid_view),
    path('', user_detail_view),
    path('<int:uid>/follow', user_follow_view),
    path('<int:uid>/isfollow', get_is_follower),
    path('<int:uid>/update', ChangProfileView.as_view())
]
