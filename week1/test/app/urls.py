from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.index, name='index'),
    path('add/', views.add, name='add')
]