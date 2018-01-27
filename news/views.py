# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from models import News


def news_list(request):
	news = News.objects.all().order_by('-pk')
	return render(request, 'news.html', {'news': news})

def news_detail(request, pk):
	News.objects.filter(pk=pk).update(score=F("score") + 1)
	news = News.objects.get(pk=pk)
	return render(request, 'news_det.html', {'news':news})
	#return HttpResponse('<h1>Detail news %s</h1>' % news.description)