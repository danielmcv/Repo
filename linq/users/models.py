# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.functions import get_filename

# Create your models here.
def get_user_filename(instance, filename):
	name, ext = os.path.splitext(filename)

	return 'users/%s' % get_filename(ext)


class User(AbstractUser):
	"""docstring for User"""
	bio = models.TextField(max_length=500, verbose_name='Biografia', blank=True)
	avatar = models.ImageField(upload_to=get_user_filename, verbose_name='Avatar', blank=True)
	facebook = models.CharField(max_length=50, verbose_name='Facebook', blank=True)
	twitter = models.CharField(max_length=50, verbose_name='Twitter',blank=True)

	class Meta:
		db_table = 'users'
		verbose_name = 'Usuario'
		verbose_name_plural = 'usuarios'

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)
		
			


		
		
