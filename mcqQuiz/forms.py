from django import forms
from mcqQuiz.models import *

class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ['subject', 'total_questions']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'option1', 'option2', 'option3', 'option4', 'correct_answer']

        labels = {
            'question_text' : 'Question',
            'option1': 'OPTION 1',
            'option2': "OPTION 2",
            'option3': 'OPTION 3',
            'option4': 'OPTION 4',
            'correct_answer': 'Correct Answer'
        }