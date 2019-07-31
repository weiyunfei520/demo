import json

from django.http import JsonResponse
from django.views import View

from books.models import BookInfo


class BooksView(View):
    def get(self, request):
        """
        获取所有图书
        :param request:
        :return:
        """
        books = BookInfo.objects.all()
        book_list = []
        for book in books:
            book_list.append({
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment
            })
        return JsonResponse({'blist': book_list})

    def post(self, request):
        """
        保存图书
        :param request:
        :return:
        """
        data = json.loads(request.body.decode())
        btitle = data.get('btitle')
        if btitle is None:
            return JsonResponse({'error': '缺少btitle字段'}, status=400)
        if len(btitle) > 20:
            return JsonResponse({'error': 'btitle字段过长'}, status=400)
        book = BookInfo.objects.create(**data)
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })


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
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

    def put(self, request, pk):
        """
        更新图书
        :param request:
        :param pk:
        :return:
        """
        data = json.loads(request.body.decode())
        btitle = data.get('btitle')
        if btitle is None:
            return JsonResponse({'error': '缺少btitle字段'}, status=400)
        if len(btitle) > 20:
            return JsonResponse({'error': 'btitle子盾过长'}, status=400)
        BookInfo.objects.filter(id=pk).update(**data)
        try:
            book = BookInfo.objects.get(id=pk)
        except:
            return JsonResponse({'error':'图书不存在'}, status=400)
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

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
        #物理删除
        book.delete()
        #逻辑删除
        # book.is_delete = True
        # book.save()
        return JsonResponse({})

