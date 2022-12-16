from django.urls import path
from . import views

app_name = 'classroom'

# domain.com/classroom
urlpatterns = [
    # path('', views.home_view, name='home'), # path expects a function!
    path('', views.HomeView.as_view(), name='home'), # 클래스를 가지고 경로에 대한 함수를 반환
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'), 
    path('contact/', views.ContactFormView.as_view(), name='contact'), 
]