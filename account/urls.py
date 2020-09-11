from .views import (home, base_index, studentSignup, TeacherSignup)

from django.urls import include, path
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from account import views



urlpatterns = [

    path('', views.home, name = 'home'),
    path('base_index/',views.base_index, name='base_index'),
    path('signup/', views.studentSignup, name='signup'),
    path('teacherSignup/', views.TeacherSignup, name='teacherSignup'),
    path('login/', auth_views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': 'index'}, name='logout'),
   # path('account/', include('django.contrib.auth.urls')),
   # path('nested_admin/', include('nested_admin.urls')),


]