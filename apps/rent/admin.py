from django.contrib import admin

from apps.rent.models import PrivateOwner, Property, Room, Category, Street, City, Client, Lease, Payment, Viewing, \
    Registration


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_number', 'street', 'city', 'postcode',
                    'category', 'rooms', 'rent', 'owner_number')

    prepopulated_fields = {'slug': ('property_number',)}
    search_fields = ('property_number', 'street', 'city', 'rooms')


@admin.register(PrivateOwner)
class PrivateOwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_number', 'first_name', 'last_name',
                    'address', 'tel_number')

    prepopulated_fields = {'slug': ('owner_number',)}


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'first_name', 'last_name',
                    'tel_number', 'pref_type', 'max_rent')

    prepopulated_fields = {'slug': ('client_number',)}

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('lease_number', 'slug', 'property_number',
                    'client_number', 'rent', 'payment_method',
                    'deposit', 'paid', 'rent_start', 'rent_finish',
                    'duration')
    prepopulated_fields = {'slug': ('lease_number',)}


@admin.register(Viewing)
class ViewingAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'property_number',
                    'view_date', 'comment')


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('client_number', 'branch_number',
                    'staff_number', 'date_joined')
