from django.conf.urls import url
from django.urls import path

from .views import home_view, articles_list_view, articles_detail_view, articles_create_view, articles_delete_view, \
    articles_action_view

urlpatterns = [
    path('', articles_list_view, name='list'),
    path('create/', articles_create_view, name='create'),
    path('<int:article_id>/delete/', articles_delete_view, name='delete'),
    path('<int:article_id>/', articles_detail_view, name='list'),
    path('action/', articles_action_view, name='action')
]
