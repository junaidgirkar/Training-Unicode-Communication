from django import forms
from .models import Quiz, Question


class QuizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = ['subject', 'total_questions']


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question_text', 'option1', 'option2',
                  'option3', 'option4', 'correct_answer']
        labels = {
            "question_text": "Question",
            "option1": "Option 1",
            "option2": "Option 2",
            "option3": "Option 3",
            "option4": "Option 4",
            "correct_answer": "Correct Answer"
        }
