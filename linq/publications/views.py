# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from django.template.loader import render_to_string

from .forms import PostForm
from .models import Post
# Create your views here.

def post_add(request):
	form = PostForm()
	context = {
		"form": form,
	}
	return render(request ,"publications/post_form.html", context)
