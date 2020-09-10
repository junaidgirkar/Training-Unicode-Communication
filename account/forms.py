from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms.widgets import RadioSelect
from django.db import transaction
from django.forms.utils import ValidationError

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    CHOICES=[('is_student','STUDENT'),('is_teacher','TEACHER')]
    role = forms.CharField(max_length=100,required=True, help_text='STUDENT/TEACHER')
    #type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    #is_student = forms.BooleanField()
    #is_teacher = forms.BooleanField()
    

    class Meta:
        model = Student
        fields = ('username', 'first_name', 'last_name','role', 'email', 'password1', 'password2', )

class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    role = forms.CharField(max_length=100, required=True,help_text='STUDENT/TEACHER')
    #is_student = forms.BooleanField()
    #is_teacher = forms.BooleanField()
    

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name','role', 'email', 'password1', 'password2', )
        



class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ['topic','total_marks']

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question_text','choice1','choice2','choice3','choice4','correct_choice']
        labels = {
            "question_text" : "Question",
            "choice1" : "Option 1",
            "choice2" : "Option 2",
            "choice3" : "Option 3",
            "choice4" : "Option 4",
            "correct_choice" : "Correct Answer"
        }