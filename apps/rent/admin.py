from django.contrib import admin

from apps.rent.models import PrivateOwner, Realty, Room, Type, Street, City, Client, Lease, Payment


@admin.register(Realty)
class RealtyAdmin(admin.ModelAdmin):
    list_display = ('property_number', 'street', 'city', 'postcode',
                    'type', 'rooms', 'rent', 'owner_number')

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
                    'address', 'tel_number', 'pref_type', 'max_rent')

    prepopulated_fields = {'slug': ('client_number',)}

@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('lease_number', 'slug', 'property_number',
                    'client_number', 'rent', 'payment_method',
                    'deposit', 'paid', 'rent_start', 'rent_finish',
                    'duration')
    prepopulated_fields = {'slug': ('lease_number',)}


admin.site.register(Room)
admin.site.register(Type)
admin.site.register(City)
admin.site.register(Payment)
