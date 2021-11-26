from django import forms

from apps.orders.models import Order
from apps.rent.models import Realty


class OrderModelForm(forms.ModelForm):
    realty = forms.ModelChoiceField(queryset=Realty.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['realty', 'name', 'phone_number', 'comment']
