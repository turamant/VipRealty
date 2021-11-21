from django import forms

from apps.orders.models import Order
from apps.rent.models import Property


class OrderModelForm(forms.ModelForm):
    _property = forms.ModelChoiceField(queryset=Property.objects.all(),
                                  widget=forms.HiddenInput())
    class Meta:
        model = Order
        fields = ['_property', 'name', 'phone_number', 'comment']
