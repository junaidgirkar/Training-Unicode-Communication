from account import views
from django.urls import include, path
from django.contrib.auth import login, logout


urlpatterns = [

    path('', views.home, name = 'home'),
    path('index/',views.index, name='index'),
    path('signup/', views.studentSignup, name='signup'),
    path('teacherSignup/', views.TeacherSignup, name='teacherSignup'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')),

    ]
