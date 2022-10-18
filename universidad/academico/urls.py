from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrarCurso/', views.registrarCurso, name='registrarCurso'),
    path('eliminarCurso/<str:codigo>', views.eliminarCurso, name='eliminarCurso'),
    path('edicionCurso/<str:codigo>', views.edicionCurso, name='edicionCurso'),
    path('editarCurso', views.editarCurso, name='editarCurso'),
]