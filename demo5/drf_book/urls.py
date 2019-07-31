from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^drf_books/$', views.BooksView.as_view()),
    url(r'^drf_books/(?P<pk>\d+)/$', views.BookView.as_view()),

]