from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('real', 'name', 'phone_number', 'create_date')
    prepopulated_fields = {'slug': ('name',)}

