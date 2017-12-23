# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):
	'''News Model'''
	class Meta(object):
		verbose_name = u"Новость"
		verbose_name_plural = u"Новости"

	tittle = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Название")

	tags = models.CharField(
		max_length=256,
		blank=False,
		default='',
		verbose_name=u"Теги")

	image = models.ImageField(
		blank=True,
		verbose_name=u"Баннер",
		null=True)

	description = models.CharField(
		max_length=1024,
		blank=False,
		verbose_name=u"Описание")

	text = RichTextUploadingField(
		blank=True, 
		default='',
		verbose_name=u"Текст новости")

	date = models.DateField(
		blank=False,
		verbose_name=u"Дата создания",
		null=False)


	def __unicode__(self):
		return u"%s %s %s" % (self.pk, self.tittle, self.date)