from account.views import *

from django.urls import include, path
from django.contrib.auth import login, logout
from mcqQuiz import views



urlpatterns = [
    path('', views.index, name = 'index'),
    path('create-quiz/', views.create_quiz, name='create_quiz'),
    path('questions/', views.add_questions, name='questions'),

    path('display/<quiz_id>', views.display, name='display'),
    path('delete/<quiz_id>',views.delete,name='delete'),
    path('update/<question_id>',views.update,name='update'),
    path('result/<quiz_id>', views.result, name='result'),
    path('result/<quiz_id>/<student_id>', views.result, name='result'),
    path('result-list/<quiz_id>', views.result_list, name='result_list')

]