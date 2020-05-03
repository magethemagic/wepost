from abc import ABC

from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from article.models import Article, Tag, Comment
from tweetme2 import settings

MAX_BLOG_LENGTH = settings.MAX_BLOG_LENGTH

ARTICLE_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    user_id = serializers.IntegerField(source='user.id')

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user_id', 'user_name', 'article']


class ArticleActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    @staticmethod
    def validate_action(value):
        value = value.lower().strip()
        if value not in ARTICLE_ACTION_OPTIONS:
            raise serializers.ValidationError("NOT A VALID ACTION")
        return value


class ArticleCreateSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'timestamp', 'content', 'likes_count']

    @staticmethod
    def validate_content(value):
        if len(value) > MAX_BLOG_LENGTH:
            raise serializers.ValidationError("长度不能超过140个字")
        return value

    @staticmethod
    def get_likes_count(obj):
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

    tags = TagSerializer(many=True, read_only=True)

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author_name', 'author_id', 'timestamp', 'content', 'likes_count', 'is_retweet', 'parent',
                  'tags', 'comments']

    @staticmethod
    def get_likes_count(obj):
        return obj.likes.count()


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'timestamp']


class ArticlePagination(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 20
