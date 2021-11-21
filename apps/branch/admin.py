from django.contrib import admin

from apps.branch.models import Branch, Staff


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch_number', 'street', 'city', 'postcode')

    search_fields = ('street', 'city')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_number', 'first_name', 'last_name',
                    'position', 'sex', 'date_of_birthday',
                    'salary', 'branch_number')

    prepopulated_fields = {'slug': ('last_name', 'staff_number')}

    search_fields = ('position', 'last_name')

