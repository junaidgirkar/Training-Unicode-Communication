from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.create_view, name='create_view'),
    path('list', views.list_view, name='list_view'),

]
