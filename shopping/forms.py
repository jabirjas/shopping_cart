from .models import Product
from django import forms
# from django.forms.widgets import TextInput, Textarea
# from django.utils.translation import ugettext_lazy as _


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'