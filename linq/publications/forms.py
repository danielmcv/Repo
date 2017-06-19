# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
		sale_image=forms.CharField()	

