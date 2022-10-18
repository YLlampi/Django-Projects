from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<id>', views.edit_task, name='edit'),
    path('completed/<id>', views.completed, name='completed'),
    path('delete/<id>', views.delete_task, name='delete'),
    path('filter/<choice>', views.filter_priority, name='priority'),
    path('status/<choice>', views.filter_status, name='status'),
]
