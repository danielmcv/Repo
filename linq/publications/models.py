# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from users.models import User

# Create your models here.
class Post(models.Model):
	"""docstring for Post"""
	posted_by = models.ForeignKey(User)
	sale_image = models.ImageField()
	date = models.DateTimeField(auto_now_add=True)
	price = models.CharField(max_length=30)
	description = models.CharField(max_length=150)
	verified = models.BooleanField(default=False)

class Comments(models.Model):
	"""docstring for Comments"""
	commented_by = models.ForeignKey(User)
	comment = models.CharField(max_length=140)
	comment_date = models.DateTimeField()
		
		
	



		

		