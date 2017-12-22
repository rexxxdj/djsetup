# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from models import News


def news_list(request):
	news = News.objects.all()

	return render(request, 'news.html', {'news': news})

def news_detail(request, pk):
	#return render(request, 'news_det.html', {'news':news.filter})
	return HttpResponse('<h1>Detail news %s</h1>' % pk)