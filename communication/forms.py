from django import forms
from .models import Quiz

class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = [
            'question',
            'option1',
            'option2',
            'option3',
            'option4',
            'correctAnswer'
        ]
