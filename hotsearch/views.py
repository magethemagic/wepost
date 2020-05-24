import datetime

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hotsearch.models import SearchKey
from hotsearch.serializers import HotSearchSerializer


def judge(search_key):
    if search_key == '':
        return
    now = timezone.now()
    keys = SearchKey.objects.filter(key_content=search_key)
    if keys:
        key = keys.first()
        if key.is_deleted:
            key.timestamp = now
            key.is_deleted = False
            key.count = 1
        else:
            key.count += 1
        key.save()
    else:
        SearchKey.objects.create(key_content=search_key).save()


def update():
    now = timezone.now()
    start = now - timezone.timedelta(hours=0, minutes=59, seconds=59)
    keys = SearchKey.objects.all()
    for key in keys:
        if key.timestamp < start:
            key.is_deleted = True
            key.count = 0
            key.save()


def get_hotsearch_list():
    return SearchKey.objects.filter(is_deleted=False).order_by('-count')[:10]


@api_view(['GET'])
def hot_search_list(request):
    search_key = request.GET.get('search')
    if search_key and search_key != '':
        judge(search_key)
    update()
    serializer = HotSearchSerializer(get_hotsearch_list(), many=True)
    return Response(serializer.data, status=200)
