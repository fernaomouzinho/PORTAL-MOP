from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from .models import Division, DG, OtherDiv
from django_summernote.widgets import SummernoteWidget


class DateInput(forms.DateInput):
	input_type = 'date'

class DGForm(forms.ModelForm):
	desc_tt = forms.CharField(label="Deskrisaun (TT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	desc_pt = forms.CharField(label="Deskrisaun (PT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	desc_en = forms.CharField(label="Deskrisaun (EN)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = DG
		fields = ['code','name_tt','name_pt','name_en','desc_tt','desc_pt','desc_en','image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('code', css_class='form-group col-md-3 mb-0'),
				Column('name_tt', css_class='form-group col-md-9 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('name_pt', css_class='form-group col-md-6 mb-0'),
				Column('name_en', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_tt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_pt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_en', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class DivisionForm(forms.ModelForm):
	desc_tt = forms.CharField(label="Deskrisaun (TT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	desc_pt = forms.CharField(label="Deskrisaun (PT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	desc_en = forms.CharField(label="Deskrisaun (EN)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Division
		fields = ['code','name_tt','name_pt','name_en','desc_tt','desc_pt','desc_en','image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('code', css_class='form-group col-md-3 mb-0'),
				Column('name_tt', css_class='form-group col-md-9 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('name_pt', css_class='form-group col-md-6 mb-0'),
				Column('name_en', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_tt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_pt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_en', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class OtherDivForm(forms.ModelForm):
	desc_tt = forms.CharField(label="Deskrisaun (TT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	desc_pt = forms.CharField(label="Deskrisaun (PT)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	desc_en = forms.CharField(label="Deskrisaun (EN)", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = OtherDiv
		fields = ['code','name_tt','name_pt','name_en','desc_tt','desc_pt','desc_en','image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('code', css_class='form-group col-md-3 mb-0'),
				Column('name_tt', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('name_pt', css_class='form-group col-md-6 mb-0'),
				Column('name_en', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_tt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_pt', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc_en', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)
