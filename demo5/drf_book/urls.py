from django.conf.urls import url
from . import views, apiviews

urlpatterns = [
    # View
    url(r'^drf_books/$', views.BooksView.as_view()),
    url(r'^drf_books/(?P<pk>\d+)/$', views.BookView.as_view()),
    # APIView
    url(r'^drf_apiviewbooks/$', apiviews.BooksAPIView.as_view()),
    url(r'^drf_apiviewbooks/(?P<pk>\d+)/$', apiviews.BookAPIView.as_view()),
]