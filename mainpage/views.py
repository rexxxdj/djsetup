# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from news.models import News


def main_page(request):
	news = News.objects.all().order_by('-pk')
	return render(request, 'mainpage.html', {'news': news})