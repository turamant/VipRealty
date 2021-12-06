from django.contrib import admin

from apps.branch.models import Branch, Staff


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'created_by')

    search_fields = ('name',)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_number', 'first_name', 'last_name',
                    'position', 'sex', 'date_of_birthday',
                    'salary', 'branch_name')

    prepopulated_fields = {'slug': ('last_name', 'staff_number')}

    search_fields = ('position', 'last_name')

