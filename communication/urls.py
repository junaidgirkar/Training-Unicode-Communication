from . import views
from django.urls import path

urlpatterns = [
    path('', views.create_view, name='create_view'),
    path('list', views.list_view, name='list_view'),
    path('<id>', views.detail_view, name='detail_view'),
    path('<id>/update', views.update_view, name='update_view'),

]
