from django.conf.urls import url
from . import views, views_restful

urlpatterns = [
    # 前后端不分离
    # url(r'^books/$', views.BookView.as_view()),
    # url(r'^heros/$', views.HeroView.as_view()),
    # 前后端分离
    url(r'^books/$', views_restful.BookView.as_view()),
]