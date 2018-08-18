from django import forms
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, HTML, Layout, Submit

from products.models import Bouquet

class BouquetForm(ModelForm):
    class Meta:
        model = Bouquet
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(BouquetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.disable_csrf = False
        self.helper.form_tag = False
        
        self.helper.layout = Layout(
            Div(
                HTML('<h5 class="text-center space-top">Bouquet Details</h5>\
                    <div class="spacer spacer-line border-primary">&nbsp;</div>'),
            ),
            Div(
                Div('name', css_class='col-md-3'),
                Div('description', css_class='col-md-6'),
            css_class='row'),
            Div(
                HTML('<h5 class="text-center  space-top">Bouquet Specifications</h5>\
                    <div class="spacer spacer-line border-primary">&nbsp;</div>'),
            ),
            Div(
                Div('max_qty', css_class='col-md-2'),
                Div('size', css_class='col-md-2'),
                Div('price', css_class='col-md-2'),
                Div('upsize', css_class='col-md-2'),
                Div('upprice', css_class='col-md-2'),
            css_class='row'),
        )
