from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from multimedia.models import Album, Gallery, Banner, Video
from django_summernote.widgets import SummernoteWidget

class DateInput(forms.DateInput):
	input_type = 'date'

class AlbumForm(forms.ModelForm):	
	desc_tt = forms.CharField(label="Deskrisaun (TT)")
	desc_pt = forms.CharField(label="Deskrisaun (PT)", required=False)
	desc_en = forms.CharField(label="Deskrisaun (EN)", required=False)
	class Meta:
		model = Album
		fields = ['cat','desc_tt','desc_pt','desc_en','image']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('cat', css_class='form-group col-md-3 mb-0'),	
				Column('image', css_class='form-group col-md-9 mb-0'),
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
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class GalleryForm(forms.ModelForm):
	desc_tt = forms.CharField(label="Deskrisaun (TT)")
	desc_pt = forms.CharField(label="Deskrisaun (PT)", required=False)
	desc_en = forms.CharField(label="Deskrisaun (EN)", required=False)
	class Meta:
		model = Gallery
		fields = ['desc_tt','desc_pt','desc_en','image']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
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
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class BannerForm(forms.ModelForm):
	desc_tt = forms.CharField(label="Deskrisaun (TT)")
	desc_pt = forms.CharField(label="Deskrisaun (PT)", required=False)
	desc_en = forms.CharField(label="Deskrisaun (EN)", required=False)
	class Meta:
		model = Banner
		fields = ['name','desc_tt','desc_pt','desc_en','image','is_active','attr']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-4 mb-0'),	
				Column('is_active', css_class='form-group col-md-3 mb-0'),
				Column('attr', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0'),
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
			HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
		)

class VideoForm(forms.ModelForm):
	date = forms.DateField(label="Data Publika", widget=DateInput())
	desc = forms.CharField(label="Deskrisaun", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
	class Meta:
		model = Video
		fields = ['language','source','title','embed_url','date','desc']
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('language', css_class='form-group col-md-3 mb-0'),
				Column('source', css_class='form-group col-md-3 mb-0'),
				Column('embed_url', css_class='form-group col-md-3 mb-0'),
				Column('date', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('title', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('desc', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-primary" type="submit"> Rai <i class="fa fa-save"></i></button> """)
		)
