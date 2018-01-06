# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib import messages
from django.core.mail import mail_admins
from django.views.generic.edit import CreateView, FormView
from django.core.urlresolvers import reverse_lazy,reverse
from datetime import datetime
from about.models import Feedback
from about.forms import FeedbackForm
from django.conf import settings

class FeedbackView(CreateView):
	model = Feedback
	template_name = "contact.html"
	success_url = reverse_lazy('about')
	form_class = FeedbackForm	

	def form_valid(self,form):
		feedback = form.save()
		mail_admins(feedback.subject, feedback.message, fail_silently=False)
		messages.success(self.request, u"Спасибо за ваш отзыв! Мы свяжемся с вами очень скоро!")
		return super(FeedbackView, self).form_valid(form)