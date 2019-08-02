from django.shortcuts import render

# Create your views here.


import json

from django.http import JsonResponse
from django.views import View

from books.models import BookInfo
from drf_book.serializer import BookInfoSerializer, BookInfoModelSerializer


class BooksView(View):
    def get(self, request):
        """
        获取所有图书
        :param request:
        :return:
        """
        books = BookInfo.objects.all()
        # book_list = []
        # for book in books:
        #     book_list.append({
        #         'id': book.id,
        #         'btitle': book.btitle,
        #         'bpub_date': book.bpub_date,
        #         'bread': book.bread,
        #         'bcomment': book.bcomment
        #     })
        # ser = BookInfoSerializer(books, many=True)
        ser = BookInfoModelSerializer(books, many=True)
        print(ser.data)
        return JsonResponse({'blist': ser.data})

    def post(self, request):
        """
        保存图书
        :param request:
        :return:
        """
        data = json.loads(request.body.decode())
        # btitle = data.get('btitle')
        # if btitle is None:
        #     return JsonResponse({'error': '缺少btitle字段'}, status=400)
        # if len(btitle) > 20:
        #     return JsonResponse({'error': 'btitle字段过长'}, status=400)
        # book = BookInfo.objects.create(**data)
        # return JsonResponse({
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment
        # })
        ser = BookInfoSerializer(data=data)
        # is_valid() 序列化器提供的验证方法
        # ser.is_valid()
        try:
            ser.is_valid(raise_exception=True)  # 验证失败抛出异常
        # 获取验证状态信息
        # data = ser.errors
        except:
            return JsonResponse({'error': ser.errors}, status=400)
        # print(data)
        # 保存数据
        ser.save()
        return JsonResponse(ser.data)


class BookView(View):
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
        # return JsonResponse({
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment
        # })
        return JsonResponse(ser.data)

    def put(self, request, pk):
        """
        更新图书
        :param request:
        :param pk:
        :return:
        """
        data = json.loads(request.body.decode())
        # btitle = data.get('btitle')
        # if btitle is None:
        #     return JsonResponse({'error': '缺少btitle字段'}, status=400)
        # if len(btitle) > 20:
        #     return JsonResponse({'error': 'btitle子盾过长'}, status=400)
        # BookInfo.objects.filter(id=pk).update(**data)
        # try:
        #     book = BookInfo.objects.get(id=pk)
        # except:
        #     return JsonResponse({'error': '图书不存在'}, status=400)
        # return JsonResponse({
        #     'id': book.id,
        #     'btitle': book.btitle,
        #     'bpub_date': book.bpub_date,
        #     'bread': book.bread,
        #     'bcomment': book.bcomment
        # })
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error': '!!!!'}, status=400)
        # 验证数据 更新数据时需要在初始化时传递更新对象
        ser = BookInfoSerializer(instance=book, data=data)
        try:
            ser.is_valid(raise_exception=True)
        except:
            return JsonResponse({'error': ser.errors}, status=400)
        ser.save()
        return JsonResponse(ser.data)

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
            return JsonResponse({'error': '图书不存在'}, status=400)
        # 物理删除
        book.delete()
        # 逻辑删除
        book.is_delete = True
        book.save()
        return JsonResponse({})
