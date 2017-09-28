from django.conf.urls import url 
from . import views 
from .views import Stores, Products
urlpatterns=[ 
	url(r'^$',				Stores.as_view(), 	name="store"), #show store, add to store
#	url(), #?
	url(r'^(?P<id>[0-9]+)$', Products.as_view(),name="products"), #edit, remove products
	url(r'^(?P<id>[0-9]+)/delete$', views.delete ,name="delete"), #edit, remove products
] 
