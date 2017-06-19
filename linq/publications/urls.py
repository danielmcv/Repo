# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from publications.models import Post
from . import views

urlpatterns = [ 
	url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
	template_name="publications/home.html")),
	url(r'^post/add/$', views.post_add, name='post_add'),

]