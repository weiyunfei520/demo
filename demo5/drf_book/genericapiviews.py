from django.shortcuts import render

# Create your views here.


import json

from django.http import JsonResponse
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import BookInfo
from drf_book.serializer import BookInfoSerializer, BookInfoModelSerializer


class BooksGenericAPIView(GenericAPIView):

    # 指定查询集
    queryset = BookInfo.objects.all()
    # 指定序列化器
    serializer_class = BookInfoSerializer

    def get(self, request):
        """
        获取所有图书
        :param request:
        :return:
        """
        # 查询图书表中的所有图书数据 get_queryset获取查询集中的所有数据
        books = self.get_queryset()
        # 调用图书序列化器类初始化生序列化器对象get_serializer调用指定的序列化器进行初始化操作
        ser = self.get_serializer(books, many=True)
        print(ser.data)
        return Response({'blist': ser.data})

    def post(self, request):
        """
        保存图书
        :param request:
        :return:
        """
        # 1、获取前端传递的数据
        data = request.data
        # 2、验证数据 序列化器初始化时，将需要验证的数据传递给data
        ser = self.get_serializer(data=data)
        try:
            ser.is_valid(raise_exception=True)  # 验证失败抛出异常
        # 获取验证状态信息
        except:
            return Response({'error': ser.errors}, status=400)
        # 保存数据
        ser.save()
        return Response(ser.data)


class BookGenericAPIView(GenericAPIView):
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
        """
        获取单一图书
        :param request:
        :return:
        """
        # get方法查询不到抛出异常  filter方法查询不到 返回空的查询集 []
        try:
            # get_object获取查询集中的单一数据对象
            book = self.get_object()
        except:
            return JsonResponse({'error': '图书不存在'}, status=400)
        # 调用图书序列化器类初始化生序列化器对象
        ser = self.get_serializer(book)
        return Response(ser.data)

    def put(self, request, pk):
        """
        更新图书
        :param request:
        :param pk:
        :return:
        """
        data = request.data
        try:
            # get_object获取查询集中单一数据对象
            book = self.get_object()
        except:
            return Response({'error': '!!!!'}, status=400)
        # 验证数据 更新数据时需要在初始化时传递更新对象
        ser = self.get_serializer(instance=book, data=data)
        try:
            ser.is_valid(raise_exception=True)
        except:
            return Response({'error': ser.errors}, status=400)
        ser.save()
        return Response(ser.data)

    def delete(self, request, pk):
        """
        删除图书
        :param request:
        :param pk:
        :return:
        """
        try:
            book = self.get_object()
        except:
            return Response({'error': '图书不存在'}, status=400)
        # 物理删除
        book.delete()
        # 逻辑删除
        # book.is_delete = True
        book.save()
        return Response({})
