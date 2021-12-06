from django.forms import ModelForm

from apps.rent.models import Realty


class RealtyForm(ModelForm):
    class Meta:
        model = Realty
        fields = ['category', 'image', 'description', 'due_back', 'rent_status',
                  'realty_number', 'street', 'city', 'postcode', 'type_realty',
                  'rooms', 'rent', 'owner_number', 'staff_number',
                  'branch_number']