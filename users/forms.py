from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import User, Group

class DateInput(forms.DateInput):
	input_type = 'date'

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','first_name']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('first_name', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('username', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('email', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <button class="btn btn-sm btn-primary" type="submit">Altera <i class="fa fa-save"></i></button> """)
		)

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(required=False)
	class Meta:
		model = User
		fields = ['username','password','email']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['group'] = forms.ModelChoiceField(
            queryset=Group.objects.all(),
            empty_label='No group'
        )
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('username', css_class='form-group col-md-6 mb-0'),
				Column('password', css_class='form-group col-md-6 mb-0'),
				Column('email', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <br><button type="submit" class="btn btn-sm btn-success btn-icon-text"><i class="mdi mdi-content-save"></i> Save </button> """)
		)
