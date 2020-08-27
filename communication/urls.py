from . import views
from django.urls import path

urlpatterns = [
    path('', views.create_view.as_view(), name='create_view'),
    path('list', views.list_view.as_view(), name='list_view'),
    path('<id>', views.detail_view.as_view(), name='detail_view'),
    path('<id>/update', views.update_view.as_view(), name='update_view'),
    path('<id>/delete', views.delete_view.as_view(), name='delete_view'),
    path('result', views.result_view, name='result_view'),

]
