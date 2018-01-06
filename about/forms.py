from django import forms
from models import Feedback
from django.forms import ModelForm

class FeedbackForm(forms.ModelForm):
	error_css_class = 'class-error'
	required_css_class = 'form-group'
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'

	def as_div(self):
		return self._html_output(
    		normal_row = u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
    		error_row = u'<div class="error">%s</div>',
    		row_ender = '</div>',
    		help_text_html = u'<div class="hefp-text">%s</div>',
    		errors_on_separate_row = False)

	class Meta:
		model = Feedback
		fields = '__all__'
