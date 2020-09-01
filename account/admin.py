from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Teacher, StudentDetail


# Register your models here.

class BaseUserAdmin(UserAdmin):
    list_display = ['email', 'is_admin', 'is_student', 'is_teacher']
    search_fields = ("email", 'sap_id', 'is_admin', 'is_student', 'is_teacher')
    readonly_fields = (
        'date_joined',
        'last_login',
    )

    filter_horizontal =()
    list_filter = ()
    fieldsets = ()

class StudentAdmin(UserAdmin):
    list_display = ('email','sap_id', 'department', 'year')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class TeacherAdmin(UserAdmin):
    list_display = ('email', 'teacher_sap_id', 'subject', 'teachingExperience')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class StudentDisplayAdmin(UserAdmin):
    list_display = ['email', 'sap_id', 'f_name']
    ordering = ['email']
    search_fields = ['email']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.unregister(Group)
admin.site.register(User, BaseUserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(StudentDetail, StudentDisplayAdmin)

