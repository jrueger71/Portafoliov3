from django.urls import path
from proyectosapp import views

urlpatterns = [
    path('', views.proyecto_list, name='proyectos'),
    path('<int:pk>/', views.proyecto_detail, name='proyecto_detail'),
]