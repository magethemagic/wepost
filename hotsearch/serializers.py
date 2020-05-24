from rest_framework import serializers

from hotsearch.models import SearchKey


class HotSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchKey
        fields = '__all__'
