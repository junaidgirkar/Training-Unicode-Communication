from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.index,name='index'),
    path('create-info/',views.create_info,name='create_info'),
    path('create/',views.create,name='create'),
    path('display/<quiz_id>',views.display,name='display'),
    path('delete/<quiz_id>',views.delete,name='delete'),
    path('update/<question_id>',views.update,name='update'),
    path('result/<quiz_id>',views.result,name='result'),
    path('result/<quiz_id>/<student_id>',views.result,name='result'),
    path('result-list/<quiz_id>',views.result_list,name='result_list')

    
]    