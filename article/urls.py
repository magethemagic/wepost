from django.urls import path

from .views import (articles_list_view,
                    articles_detail_view,
                    articles_create_view,
                    articles_delete_view,
                    articles_action_view,
                    comment_create_view, ArticleListApiView)

urlpatterns = [
    path('list/', ArticleListApiView.as_view(), name='list'),
    path('', articles_list_view, name='list2'),
    path('create/', articles_create_view, name='create'),
    path('<int:article_id>/delete/', articles_delete_view, name='delete'),
    path('<int:article_id>/', articles_detail_view, name='list'),
    path('action/', articles_action_view, name='action'),
    path('comments/create/', comment_create_view, name='comment_create'),
]
