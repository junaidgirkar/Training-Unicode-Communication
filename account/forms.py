from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.forms import ModelForm
from .models import StudentDetail
from account.models import Student, User


class StudentDetailForm(ModelForm):
    class Meta:
        model = StudentDetail
        fields = ['email', 'sap_id', 'f_name', 'l_name', 'is_student']