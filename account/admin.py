from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student


# Register your models here.

class BaseUserAdmin(UserAdmin):
    list_display = ['email']
    search_fields = ("email", 'sap_id')
    readonly_fields = (
        'date_joined',
        'last_login',
    )

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

class StudentAdmin(UserAdmin):
    list_display = ('sap_id', 'department', 'year')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.unregister(Group)
admin.site.register(User, BaseUserAdmin)
admin.site.register(Student, StudentAdmin)

