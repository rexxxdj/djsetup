# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
	news = (
		{'id': 1,
		 'tittle': u'Pioneer DJ DDJ-XP1',
		 'date': '22.11.2017',
		 'description': 'Pioneer DJ выпустили новый контроллер для Rekordbox™DJ и Rekordbox DVS - DDJ-XP1, который имеет 32 пэда для тактильного управления точками Cues, Pad FX, Beat Jump, Sampler, Beat Loop и новыми функциями Key Shift и Keyboard, которые появились в новой версии Rekordbox™DJ 5.0. Больше информации доступно по ссылке ниже.',
		 'image': 'img/map.jpg',
		 'tags': '#tags #tags #tags'},
		 {'id': 2,
		 'tittle': u'Aiaiai TMA-1',
		 'date': '22.11.2017',
		 'description': 'Focusrite анонсировали RedNet X2P 2x2 Dante™ аудио интерфейс. Компактный и прочный, RedNet X2P, имеет два микрофонных предусилителя Red Evolution, линейный сетео выход и сетереофонический усилитель для наушников, позволяет осуществлять быстрый ввод-вывод и контролировать расширение Focusrite RedNet или других систем Dante audio-over-IP. Больше информации доступно на официальном сайте по ссылке ниже.',
		 'image': 'img/tracks.jpg',
		 'tags': '#tags #tags #tags'},
		 {'id': 3,
		 'tittle': u'Pioneer DJ DDJ-XP1',
		 'date': '22.11.2017',
		 'description': 'Pioneer DJ выпустили новый контроллер для Rekordbox™DJ и Rekordbox DVS - DDJ-XP1, который имеет 32 пэда для тактильного управления точками Cues, Pad FX, Beat Jump, Sampler, Beat Loop и новыми функциями Key Shift и Keyboard, которые появились в новой версии Rekordbox™DJ 5.0. Больше информации доступно по ссылке ниже.',
		 'image': 'img/map.jpg',
		 'tags': '#tags #tags #tags'},
	)



	return render(request, 'mainpage.html', {'news': news})