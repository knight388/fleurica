from django import forms
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, HTML, Layout, Submit

from florists.models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['questions', 'days', 'status', 'uuid', 'logo', 'banner']

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = False
        self.helper.form_tag = False
        self.fields['con_name'].label = 'Name of contact'
        self.fields['con_email'].label = 'Email'
        self.fields['con_number'].label = 'Contact No'
        self.fields['address'].widget.attrs['rows'] = 4
        self.fields['acra'].required = True
        
        self.helper.layout = Layout(
            Div(
                HTML('<h5 class="text-center">Business Details</h5>\
                    <div class="spacer spacer-line border-primary">&nbsp;</div>'),
            ),
            Div(
                Div('bname', css_class='col-md-3'),
                Div('acra', css_class='col-md-3'),
            css_class='row'),
            Div(
                HTML('<h5 class="text-center space-top">Contact Info</h5>\
                    <div class="spacer spacer-line border-primary">&nbsp;</div>'),
            ),
            Div(
                Div('con_name', css_class='col-md-3'),
                Div('con_email', css_class='col-md-3'),
                Div('con_number', css_class='col-md-3'),
                Div('address', css_class='col-md-3'),
            css_class='row'),
        )
