# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def news_list(request):
	return render(request, 'news.html', {})