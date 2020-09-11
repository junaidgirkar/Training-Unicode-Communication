from django.contrib import admin
from django.urls import path,include
from communication import views


app_name='communication'

urlpatterns=[
    path('',views.ChapterListView.as_view(),name='list'),
    path('<int:pk>/',views.QuestionDetailView.as_view(),name='detail'),
    path('create/',views.ChapterCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.QuestionUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.ChapterDeleteView.as_view(),name='delete'),
    path('student/',views.student_chp_lst,name='list_fun'),
    path('student/<int:chp_pk>/',views.question_detail,name='detail_fun'),



]
