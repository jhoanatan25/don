from django.conf.urls import url,include
from .views import *

urlpatterns =[
    url(r'^$',article,name='article'),
	url(r'car_reviews',car_reviews,name='car_reviews'),
	url(r'buying_guide',buying_guide,name='buying_guide'),
	url(r'press_room',press_room,name='press_room'),
    url(r'new/(?P<blog_name>[\w.@+-]+)',article,name='article'),
    url(r'new',article,name='article'),
    url(r'delete',delete,name='delete'),
    url(r'published',published,name='published'),
]
