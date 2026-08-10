from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML
from news.models import News, NewsImage
from django_summernote.widgets import SummernoteWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class NewsForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput(), required=True)
    image = forms.FileField(label="Upload image", required=False)
    title_tt = forms.CharField(label="Titulu Nutisia Tetum")
    title_pt = forms.CharField(label="Titulu Nutisia Portugues")
    title_en = forms.CharField(label="Titulu Nutisia English")
    content_tt = forms.CharField(label="Konteudu Tetum", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    content_pt = forms.CharField(label="Konteudu Portugues", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    content_en = forms.CharField(label="Konteudu English", widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}))
    
    class Meta:
        model = News
        fields = ['cat','title_tt','title_pt','title_en','headline_tt','headline_pt','headline_en','content_tt','content_pt','content_en','place','date']
    
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title_tt', css_class='form-group col-md-12 mb-0'),
                Column('title_pt', css_class='form-group col-md-12 mb-0'),
                Column('title_en', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                #Column('language', css_class='form-group col-md-3 mb-0'),
                Column('cat', css_class='form-group col-md-3 mb-0'),
                Column('place', css_class='form-group col-md-3 mb-0'),	
                Column('date', css_class='form-group col-md-3 mb-0'),	
                css_class='form-row'
            ),
            Row(
                Column('headline_tt', css_class='form-group col-md-12 mb-0'),
                Column('headline_pt', css_class='form-group col-md-12 mb-0'),
                Column('headline_en', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('content_tt', css_class='form-group col-md-12 mb-0'),
                Column('content_pt', css_class='form-group col-md-12 mb-0'),
                Column('content_en', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
        )

class NewsImageForm(forms.ModelForm):
    image = forms.FileField(label="Upload image", required=True)
    desc_tt = forms.CharField(label="Deskrisaun (TT)", required=False, widget=forms.Textarea(attrs={"rows":3}))
    desc_pt = forms.CharField(label="Deskrisaun (PT)", required=False, widget=forms.Textarea(attrs={"rows":3}))
    desc_en = forms.CharField(label="Deskrisaun (EN)", required=False, widget=forms.Textarea(attrs={"rows":3}))
    class Meta:
        model = NewsImage
        fields = ['desc_tt','desc_pt','desc_en','image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('desc_tt', css_class='form-group col-md-4 mb-0'),
                Column('desc_pt', css_class='form-group col-md-4 mb-0'),
                Column('desc_en', css_class='form-group col-md-4 mb-0'),		
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-12 mb-0'),		
                css_class='form-row'
            ),
            HTML(""" <button class="btn btn-primary" type="submit">Rai <i class="fa fa-save"></i></button> """)
        )