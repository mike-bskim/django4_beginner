# import imp


from django.urls import URLPattern, path
from . import views # from views import index 로 처리가능하지만 일반적으로 이렇게 처리함

urlpatterns = [
    path('', views.index, name='index') #/my_app --> PROJECT urls.py
]
