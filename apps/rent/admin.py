from django.contrib import admin

from apps.rent.models import Owner, Client, Lease, Viewing, Registration, Realty


@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    list_display = ('rent_status', 'realty_number', 'due_back', 'street', 'city', 'postcode',
                    'category', 'rooms', 'rent', 'owner_number', 'staff_number',
                    'branch_number')

    prepopulated_fields = {'slug': ('realty_number',)}
    search_fields = ('property_number', 'street', 'city', 'rooms')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_number', 'first_name', 'last_name',
                    'address', 'tel_number')

    prepopulated_fields = {'slug': ('owner_number',)}


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'first_name', 'last_name',
                    'tel_number', 'pref_category', 'pref_rooms', 'max_rent')

    prepopulated_fields = {'slug': ('client_number',)}

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('lease_number', 'realty_number', 'owner_number',
                    'client_number', 'rent', 'payment_method',
                    'deposit', 'paid', 'rent_start', 'rent_finish',
                    'duration')
    prepopulated_fields = {'slug': ('lease_number',)}


@admin.register(Viewing)
class ViewingAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'realty_number',
                    'view_date', 'comment')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'branch_number',
                    'staff_number', 'date_joined')
