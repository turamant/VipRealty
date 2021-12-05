from django import forms

from apps.rent.models import Lease, Viewing, Client
from apps.thesaurus.models import TypeRealty


class RealtyFilterForm(forms.Form):
    type_realty = forms.ModelChoiceField(queryset=TypeRealty.objects.all(), label='Тип недвижимости')

    min_rent = forms.FloatField(label='rent от', required=False)
    max_rent = forms.FloatField(label='rent до', required=False)
    min_rooms = forms.IntegerField(label='room от', required=False)
    max_rooms = forms.IntegerField(label='room до', required=False)

    ordering = forms.ChoiceField(label='сортировка', required=False, choices=[
        ['rooms', 'по количеству комнат'],
        ['rent', 'дешевые сверху'],
        ['-rent', 'дорогие сверху'],
        ['-city', 'по городам'],
        ['-street', 'по улицам'],
    ])

class LeaseCreateForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = '__all__'


class ViewingCreateForm(forms.ModelForm):
    class Meta:
        model = Viewing
        fields = ('client_number', 'realty_number', 'view_date', 'comment')

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_number', 'slug', 'first_name', 'last_name',
                  'tel_number', 'pref_category', 'pref_rooms', 'max_rent']

