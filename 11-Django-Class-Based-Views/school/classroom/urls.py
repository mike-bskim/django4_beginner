from django.urls import path
from . import views

app_name = 'classroom'

# domain.com/classroom
urlpatterns = [
    path('', views.home_view, name='home'), # path expects a function!
]