from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
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
        
        
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text', )


class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()

        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
        if not has_one_correct_answer:
            raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')


class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
        queryset=Answer.objects.none(),
        widget=forms.RadioSelect(),
        required=True,
        empty_label=None)

    class Meta:
        model = StudentAnswer
        fields = ('answer', )

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        self.fields['answer'].queryset = question.answers.order_by('text')
        
        
