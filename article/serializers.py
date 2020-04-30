from abc import ABC

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from article.models import Article
from tweetme2 import settings

MAX_BLOG_LENGTH = settings.MAX_BLOG_LENGTH

ARTICLE_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS


class ArticleActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in ARTICLE_ACTION_OPTIONS:
            raise serializers.ValidationError("NOT A VALID ACTION")
        return value


class ArticleCreateSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'timestamp', 'content', 'likes_count']

    def validate_content(self, value):
        if len(value) > MAX_BLOG_LENGTH:
            raise serializers.ValidationError("长度不能超过140个字")
        return value

    def get_likes_count(self, obj):
        return obj.likes.count()


class ArticleParentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='user.username')
    author_id = serializers.IntegerField(source='user.id')
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author_name', 'author_id', 'timestamp', 'content', 'likes_count']

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='user.username')
    author_id = serializers.IntegerField(source='user.id')
    likes_count = serializers.SerializerMethodField(read_only=True)
    parent = ArticleParentSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author_name', 'author_id', 'timestamp', 'content', 'likes_count', 'is_retweet', 'parent']

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()


class ArticlePaginations(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 20
