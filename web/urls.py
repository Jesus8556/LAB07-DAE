from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    
    path('', views.AlumnoView.as_view(),name='index'),
    path('/profesor', views.PorfesorView.as_view(),name='profesor'),
    path('eliminar/<int:pk>/', views.EliminarAlumnoView.as_view(), name='eliminar'),
    path('/profesor/eliminar/<int:pk>/', views.EliminarProfesorView.as_view(), name='eliminar2')


]