# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from models import News


def news_list(request):
	news_list = News.objects.all().order_by('-pk')
	paginator = Paginator(news_list, 4) # Show 4 news per page

	page = request.GET.get('page')
	try:
		news = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		news = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		news = paginator.page(paginator.num_pages)

	return render(request, 'news.html', {'news': news})

def news_detail(request, pk):
	News.objects.filter(pk=pk).update(score=F("score") + 1)
	news = News.objects.get(pk=pk)
	return render(request, 'news_det.html', {'news':news})
	#return HttpResponse('<h1>Detail news %s</h1>' % news.description)