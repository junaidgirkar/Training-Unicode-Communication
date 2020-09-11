from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.index,name='index'),
    path('create-info/',views.create_info,name='create_info'),
    path('create/',views.create,name='create'),
    path('display/<quiz_id>',views.display,name='display'),
    path('delete/<quiz_id>',views.delete,name='delete'),
    path('update/<question_id>',views.update,name='update')
    
]