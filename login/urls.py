from django.conf.urls import url
from . import views

urlpatterns=[
		url(r'^$',views.index),
		url(r'^loginpage/',views.loginpage),
		url(r'^inside/',views.inside,name='inside'),
		url(r'signout/',views.signout),
		url(r'catalog/',views.catalog,name='catalog'),
		url(r'books/',views.book_list_view,name='book_list_view'),
		url(r'authors/',views.author_list_view,name='author_list_view'),
		url(r'^book/(?P<pk>\d+)/$',views.book_detail,name='book_detail'),
		url(r'^author/(?P<pk>\d+)/$',views.author_detail,name='author_detail'),
		url(r'^post',views.postbook,name='postbook')
	]

			