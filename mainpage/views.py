# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from news import models as newsmodel


def main_page(request):
	news = newsmodel.News.objects.all()

	return render(request, 'mainpage.html', {'news': news})