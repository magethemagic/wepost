from rest_framework import serializers

from userprofile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    uid = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    blog_count = serializers.SerializerMethodField(read_only=True)
    follower_count = serializers.SerializerMethodField(read_only=True)
    followed_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['uid', 'gender', 'username', 'first_name', 'last_name',
                  'tel', 'email', 'desc', 'avatar', 'blog_count',
                  'follower_count', 'followed_count']

    @staticmethod
    def get_blog_count(obj):
        return obj.user.articles.count()

    @staticmethod
    def get_follower_count(obj):
        return obj.user.userprofile.followers.count()

    @staticmethod
    def get_followed_count(obj):
        return obj.user.following.count()


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['desc', 'avatar', 'tel', 'gender']
