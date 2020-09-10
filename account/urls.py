from account import views
from django.urls import include, path
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', views.home, name = 'home'),
    path('index/',views.index, name='index'),
    path('signup/', views.studentSignup, name='signup'),
    path('teacherSignup/', views.TeacherSignup, name='teacherSignup'),
    path('login/', auth_views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': 'index'}, name='logout'),
    path('account/', include('django.contrib.auth.urls')),

    ]
