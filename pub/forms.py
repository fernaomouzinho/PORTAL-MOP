from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from pub.models import Publication, Vaga, Tender
from django_summernote.widgets import SummernoteWidget


class DateInput(forms.DateInput):
	input_type = 'date'

class VagaForm(forms.ModelForm):
	date = forms.DateField(label="Data Publika", widget=DateInput(), required=True)
	desc = forms.CharField(label="Deskrisaun", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Vaga
		fields = ['language','title','date','desc','file','image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('language', css_class='form-group col-md-3 mb-0'),
				Column('title', css_class='form-group col-md-6 mb-0'),
				Column('date', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-6 mb-0'),
				Column('file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class TenderForm(forms.ModelForm):
	date = forms.DateField(label="Data Publika", widget=DateInput(), required=True)
	desc = forms.CharField(label="Deskrisaun", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Tender
		fields = ['language','title','date','desc','file','image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('language', css_class='form-group col-md-3 mb-0'),
				Column('title', css_class='form-group col-md-6 mb-0'),
				Column('date', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-6 mb-0'),
				Column('file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class PublicationForm(forms.ModelForm):
	desc = forms.CharField(label="Deskrisaun", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Publication
		fields = ['language','title','desc','file','image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('language', css_class='form-group col-md-3 mb-0'),
				Column('title', css_class='form-group col-md-9 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-6 mb-0'),
				Column('file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)
