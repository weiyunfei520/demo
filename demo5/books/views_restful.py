import json

from django.http import JsonResponse
from django.views import View

from books.models import BookInfo


class BookView(View):
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
                'becomment': book.bcomment
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
            'becomment': book.bcomment
        })


