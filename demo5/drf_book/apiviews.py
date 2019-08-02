from django.shortcuts import render

# Create your views here.


import json

from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import BookInfo
from drf_book.serializer import BookInfoSerializer, BookInfoModelSerializer


class BooksAPIView(APIView):
    def get(self, request):
        """
        获取所有图书
        :param request:
        :return:
        """
        books = BookInfo.objects.all()
        ser = BookInfoSerializer(books, many=True)
        print(ser.data)
        return Response({'blist': ser.data})

    def post(self, request):
        """
        保存图书
        :param request:
        :return:
        """
        data = request.data
        ser = BookInfoSerializer(data=data)
        try:
            ser.is_valid(raise_exception=True)  # 验证失败抛出异常
        # 获取验证状态信息
        except:
            return Response({'error': ser.errors}, status=400)
        # 保存数据
        ser.save()
        return Response(ser.data)


class BookAPIView(APIView):
    """
    获取单一图书
    更新图书
    删除图书
    """

    def get(self, request, pk):
        """
        获取单一图书
        :param request:
        :return:
        """
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '图书不存在'}, status=400)
        ser = BookInfoSerializer(book)
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
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': '!!!!'}, status=400)
        # 验证数据 更新数据时需要在初始化时传递更新对象
        ser = BookInfoSerializer(instance=book, data=data)
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
            book = BookInfo.objects.get(id=pk)
        except:
            return Response({'error': '图书不存在'}, status=400)
        # 物理删除
        book.delete()
        # 逻辑删除
        # book.is_delete = True
        book.save()
        return Response({})
