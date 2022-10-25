from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_view), # domain.com/my_app
    path('variable/', views.variable_view), # domain.com/my_app
]