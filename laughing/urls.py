from django.urls import path
from .views import *
from django.conf.urls import url


urlpatterns = [
    path('',index_view, name='index'),
    #path('',QuoteView.as_view(), name='index'),
    url(r'^search/$', display, name="disp"),
    url(r'^add/$', add_meme, name="add"),

    path('', MemeView.as_view(),name='details'),
    path('like', LikeView, name="post"),

]