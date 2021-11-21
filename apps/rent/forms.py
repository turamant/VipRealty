from django import forms


class PropertyFilterForm(forms.Form):
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
