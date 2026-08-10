from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from doc.models import Doc, Report
from django_summernote.widgets import SummernoteWidget

class DateInput(forms.DateInput):
	input_type = 'date'

class DocForm(forms.ModelForm):
	desc = forms.CharField(label="Deskrisaun (TT)", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Doc
		fields = ['doc_type','language','title','desc', 'file']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('doc_type', css_class='form-group col-md-3 mb-0'),
				Column('language', css_class='form-group col-md-3 mb-0'),
				Column('title', css_class='form-group col-md-6 mb-0'),	
				css_class='form-row'
			),
			Row(
				Column('desc', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('file', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class ReportForm(forms.ModelForm):
	date = forms.DateField(label="Data Publika", widget=DateInput(), required=True)
	desc = forms.CharField(label="Deskrisaun", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Report
		fields = ['owner','language','title','date','desc','file','image']

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
				Column('owner', css_class='form-group col-md-12 mb-0'),
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

