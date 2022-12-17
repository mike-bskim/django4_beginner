from django.urls import path
from . import views

app_name = 'classroom'

# domain.com/classroom
urlpatterns = [
    # path('', views.home_view, name='home'), # path expects a function!
    path('', views.HomeView.as_view(), name='home'), # 클래스를 가지고 경로에 대한 함수를 반환
    path('thank_you/', views.ThankYouView.as_view(), name='thank_you'), 
    path('contact/', views.ContactFormView.as_view(), name='contact'), 
    path('create_teacher/', views.TeacherCreateView.as_view(), name='create_teacher'), 
    path('list_teacher/', views.TeacherListView.as_view(), name='list_teacher'), 
    path('detail_teacher/<int:pk>', views.TeacherDetailView.as_view(), name='detail_teacher'), 
    path('update_teacher/<int:pk>', views.TeacherUpdateView.as_view(), name='update_teacher'), 
    path('delete_teacher/<int:pk>', views.TeacherDeleteView.as_view(), name='delete_teacher'), 
]