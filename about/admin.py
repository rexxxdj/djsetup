# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from about.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	model = Feedback
	list_display = ( 'name', 'from_email', 'create_date',)


admin.site.register(Feedback, FeedbackAdmin)