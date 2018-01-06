# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse_lazy

class Feedback(models.Model):
	name = models.CharField(max_length=200,
		verbose_name = 'Имя')
	from_email = models.EmailField(verbose_name = 'Email')
	subject = models.CharField(max_length=200,
		verbose_name = 'Тема')
	message =models.TextField()	
	create_date = models.DateTimeField(auto_now_add=True)

	#def __unicode__(self):
	#	return self.name
# Create your models here.
