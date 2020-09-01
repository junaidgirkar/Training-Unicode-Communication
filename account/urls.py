from account import views
from django.urls import include, path


urlpatterns = [

    #path('userdetails/',views.studentDetail, name = 'UserDetails'),
    path('display/', views.studentDetail, name = 'useDetailDisplay'),
    ]
