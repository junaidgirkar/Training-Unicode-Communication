from account import views
from django.urls import include, path
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('', views.home, name = 'home'),
    path('base_index/',views.index, name='base_index'),
    path('signup/', views.studentSignup, name='signup'),
    path('teacherSignup/', views.TeacherSignup, name='teacherSignup'),
    path('login/', auth_views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': 'index'}, name='logout'),
    path('account/', include('django.contrib.auth.urls')),
    path('nested_admin/', include('nested_admin.urls')),

    path('index/', views.index, name='index'),
    path('create-info/', views.create_info, name='create_info'),
    path('create/', views.create, name='create'),
    path('display/<quiz_id>', views.display, name='display'),
    path('delete/<quiz_id>', views.delete, name='delete'),
    path('update/<question_id>', views.update, name='update')


]