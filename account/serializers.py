from rest_framework import serializers

from account.models import UserProfile
from article.serializers import ArticleSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    blog_count = serializers.IntegerField(source='articles.count')

    # followers_count = serializers.IntegerField(source='followers.count')

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'user_desc', 'user_avatar', 'phone_number', 'blog_count']
