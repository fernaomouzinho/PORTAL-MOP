from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.db.models import Q
from django.contrib.auth.models import User
from about.models import About, Partner, Structure, Contact, ContactMun
from django_summernote.widgets import SummernoteWidget

class DateInput(forms.DateInput):
	input_type = 'date'

class AboutForm(forms.ModelForm):
	vision_tt = forms.CharField(label="Visuan (TT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	mission_tt = forms.CharField(label="Misaun (TT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	hist_tt = forms.CharField(label="Historia (TT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	vision_pt = forms.CharField(label="Visuan (PT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	mission_pt = forms.CharField(label="Misaun (PT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	hist_pt = forms.CharField(label="Historia (PT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	vision_en = forms.CharField(label="Visuan (EN)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	mission_en = forms.CharField(label="Misaun (EN)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	hist_en = forms.CharField(label="Historia (EN)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = About
		fields = ['vision_tt','mission_tt','hist_tt',\
	    		'vision_pt','mission_pt','hist_pt','vision_en','mission_en','hist_en','image']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('vision_tt', css_class='form-group col-md-6 mb-0'),
				Column('mission_tt', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('hist_tt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('vision_pt', css_class='form-group col-md-6 mb-0'),
				Column('mission_pt', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('hist_pt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('vision_en', css_class='form-group col-md-6 mb-0'),
				Column('mission_en', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('hist_en', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-sm btn-primary" type="submit">Altera <i class="fa fa-save"></i></button> """)
		)

class OrgChartForm(forms.ModelForm):
	org_chart = forms.FileField(label="Upload Organograma", required=False)
	class Meta:
		model = About
		fields = ['org_chart']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('org_chart', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-sm btn-primary" type="submit">Altera <i class="fa fa-save"></i></button> """)
		)

class StructureForm(forms.ModelForm):
	desc = forms.CharField(label="Deskrisaun Badak", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Structure
		fields = ['name','sex','image','pos','dg','div','order','desc']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-5 mb-0'),
				Column('sex', css_class='form-group col-md-2 mb-0'),
				Column('pos', css_class='form-group col-md-3 mb-0'),
				Column('order', css_class='form-group col-md-2 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('dg', css_class='form-group col-md-6 mb-0'),
				Column('div', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class ContactForm(forms.ModelForm):
	
	class Meta:
		model = Contact
		fields = ['email','phone','address']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('email', css_class='form-group col-md-3 mb-0'),
				Column('phone', css_class='form-group col-md-3 mb-0'),
				Column('address', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class ContactMunForm(forms.ModelForm):
	
	class Meta:
		model = ContactMun
		fields = ['name','mun','email','phone','address','location','lat','lng']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-8 mb-0'),
				Column('mun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('email', css_class='form-group col-md-3 mb-0'),
				Column('phone', css_class='form-group col-md-3 mb-0'),
				Column('address', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('location', css_class='form-group col-md-6 mb-0'),
				Column('lat', css_class='form-group col-md-3 mb-0'),
				Column('lng', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)
###
class PartnerForm(forms.ModelForm):
	class Meta:
		model = Partner
		fields = ['code','name','website','image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('code', css_class='form-group col-md-3 mb-0'),
				Column('name', css_class='form-group col-md-6 mb-0'),
				Column('website', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)
