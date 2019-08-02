from django.conf.urls import url
from . import views, apiviews, genericapiviews, modelmixinviews

urlpatterns = [
    # View
    url(r'^drf_books/$', views.BooksView.as_view()),
    url(r'^drf_books/(?P<pk>\d+)/$', views.BookView.as_view()),
    # APIView
    url(r'^drf_apiviewbooks/$', apiviews.BooksAPIView.as_view()),
    url(r'^drf_apiviewbooks/(?P<pk>\d+)/$', apiviews.BookAPIView.as_view()),
    # GenericAPIView
    url(r'^drf_genericapiviewbooks/$', genericapiviews.BooksGenericAPIView.as_view()),
    url(r'^drf_genericapiviewbooks/(?P<pk>\d+)/$', genericapiviews.BookGenericAPIView.as_view()),
    # ModelMixinView
    url(r'^drf_modelmixinviewbooks/$', modelmixinviews.BooksModelMixinView.as_view()),
    url(r'^drf_modelmixinviewbooks/(?P<pk>\d+)/$', modelmixinviews.BookModelMixinView.as_view()),
]