# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy
from django import forms

class Feedback(models.Model):
	name = models.CharField(max_length=200,
		verbose_name = 'Имя'		)
	from_email = models.EmailField(verbose_name = 'Email')
	subject = models.CharField(max_length=200,
		verbose_name = 'Тема сообщения')
	message = models.TextField()	
	create_date = models.DateTimeField(auto_now_add=True)

	class Meta(object):
		verbose_name = u"Отзыв"
		verbose_name_plural = u"Отзывы"
