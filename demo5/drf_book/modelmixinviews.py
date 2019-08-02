from django.shortcuts import render

# Create your views here.


import json

from django.http import JsonResponse
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.views import APIView

from books.models import BookInfo
from drf_book.serializer import BookInfoSerializer, BookInfoModelSerializer


class BooksModelMixinView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # 指定查询集
    queryset = BookInfo.objects.all()
    # 指定序列化器
    serializer_class = BookInfoSerializer

    def get(self, request):
       return self.list(request)

    def post(self, request):
        return self.create(request)


class BookModelMixinView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """
    获取单一图书
    更新图书
    删除图书
    """
    # 指定查询集
    queryset = BookInfo.objects.all()
    # 指定序列化器
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
       return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
       return self.destroy(request)
