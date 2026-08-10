from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from django_summernote.widgets import SummernoteWidget
from project.models import ProjMapG, ProjMapS, ProjMapP

class DateInput(forms.DateInput):
	input_type = 'date'

class ProjMapGForm(forms.ModelForm):
	class Meta:
		model = ProjMapG
		fields = ['subject','file']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('subject', css_class='form-group col-md-6 mb-0'),
				Column('file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class ProjMapSForm(forms.ModelForm):
	class Meta:
		model = ProjMapS
		fields = ['subject','file']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('subject', css_class='form-group col-md-6 mb-0'),
				Column('file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class ProjMapPForm(forms.ModelForm):
	class Meta:
		model = ProjMapP
		fields = ['subject','file']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('subject', css_class='form-group col-md-6 mb-0'),
				Column('file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)
