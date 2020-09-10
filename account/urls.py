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

    

    path('students/', include(([
            path('', views.QuizListView.as_view(), name='quiz_list'),
            # path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
            path('taken/', views.TakenQuizListView.as_view(), name='taken_quiz_list'),
            path('quiz/<int:pk>/', views.take_quiz, name='take_quiz'),
        ], 'classroom'), namespace='students')),

        #path('teachers/', include(([
            path('quiz/list/', views.QuizListView.as_view(), name='quiz_change_list'),
            path('quiz/add/', views.QuizCreateView.as_view(), name='quiz_add'),
            path('quiz/<int:pk>/', views.QuizUpdateView.as_view(), name='quiz_change'),
            path('quiz/<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz_delete'),
            path('quiz/<int:pk>/results/', views.QuizResultsView.as_view(), name='quiz_results'),
            path('quiz/<int:pk>/question/add/', views.question_add, name='question_add'),
            path('quiz/<int:quiz_pk>/question/<int:question_pk>/', views.question_change, name='question_change'),
            path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', views.QuestionDeleteView.as_view(), name='question_delete'),
        #], 'classroom'), namespace='teachers')),
    ]
