from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import User
from .models import Announce
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DateInput(forms.DateInput):
	input_type = 'date'

class AnnounceForm(forms.ModelForm):
	date = forms.DateField(label="Data Publika", widget=DateInput(), required=True)
	desc = forms.CharField(label="Dekrisaun", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))
	class Meta:
		model = Announce
		fields = ['type','language','title','date','desc','file','image']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('type', css_class='form-group col-md-4 mb-0'),	
				Column('language', css_class='form-group col-md-4 mb-0'),
				Column('date', css_class='form-group col-md-4 mb-0'),	
				css_class='form-row'
			),
			Row(
				Column('title', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-6 mb-0'),
				Column('file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc', css_class='form-group col-md-12 mb-0'),	
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)