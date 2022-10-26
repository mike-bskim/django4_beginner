from django.urls import path
from . import views

# register the app namespace
# RUL NAMES
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name= 'example'), # domain.com/my_app
    path('variable/', views.variable_view, name='variable'), # domain.com/my_app
]