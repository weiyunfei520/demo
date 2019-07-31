from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import BookInfo, HeroInfo
from datetime import date


class BookView(View):
    def get(self, request):
        # 增加
        # book = BookInfo(
        #     btitle='西游记',
        #     bpub_date=date(2019, 7, 1),
        #     bread=10,
        #     bcomment=10
        # )
        # book.save()
        # book = BookInfo.objects.create(
        #     btitle='红楼梦',
        #     bpub_date=date(2019, 7, 2)
        # )
        # 修改
        # book = BookInfo.objects.get(pk=6)
        # book.btitle = '红楼梦123'
        # book.save()
        # BookInfo.objects.filter(pk=5).update(btitle='西游记123')
        # 删除
        # book = BookInfo.objects.get(pk=6)
        # book.delete()
        # BookInfo.objects.filter(pk=5).delete()

        # 查询
        # blist = BookInfo.objects.all()
        # blist = BookInfo.objects.filter(pk__exact=1)
        # blist = BookInfo.objects.filter(pk=2)
        # blist = BookInfo.objects.filter(btitle__contains='传')
        # blist = BookInfo.objects.filter(btitle__endswith='部')
        # blist = BookInfo.objects.filter(btitle__isnull=False)
        # blist = BookInfo.objects.filter(pk__in=[1, 3])
        # blist = BookInfo.objects.filter(pk__gt=3)
        # blist = BookInfo.objects.filter(bpub_date__year=1980)
        # blist = BookInfo.objects.filter(bpub_date__gt=date(1980, 1, 1))
        from django.db.models import F
        # blist = BookInfo.objects.filter(bread__gt=F('bcomment'))
        # blist = BookInfo.objects.filter(bread__gt=F('bcomment') * 2)
        from django.db.models import Q
        # blist = BookInfo.objects.filter(bread__gt=20, pk__lt=3)
        # blist = BookInfo.objects.filter(Q(bread__gt=20) & Q(pk__lt=3))
        # blist = BookInfo.objects.filter(Q(bread__gt=20) | Q(pk__lt=3))
        # blist = BookInfo.objects.filter(~Q(pk=3))
        from django.db.models import Sum, Max, Min, Avg, Count
        # blist = BookInfo.objects.order_by('bcomment')
        # blist = BookInfo.objects.order_by('-bcomment')
        return render(request, 'books.html', {'blist': blist})
        # a = BookInfo.objects.count()
        # print(a)
        # a = BookInfo.objects.aggregate(Sum('bread'))
        # print(a['bread__sum'])
        # return HttpResponse('ok')


class HeroView(View):
    def get(self, request):
        # hero = HeroInfo.objects.get(pk=1)
        # hero = HeroInfo.objects.filter(pk=1)
        blist = BookInfo.objects.filter(heros__hcomment__contains='八')
        print(blist)
        return HttpResponse('ok')