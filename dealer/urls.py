from django.conf.urls import url,include
from .views import *

urlpatterns =[
	url(r'^$',dealer_page, name= 'dealer_page'),
	url(r'(?P<username>[\w.@+-]+)/(?P<page>[\w.@+-]+)/(?P<id>[\w.@+-]+)/$', dealer_page, name= 'dealer_page'),
    url(r'(?P<username>[\w.@+-]+)/(?P<page>[\w.@+-]+)/$', dealer_page, name= 'dealer_page'),
	url(r'(?P<username>[\w.@+-]+)/$',dealer_page, name= 'dealer_page'),
]
