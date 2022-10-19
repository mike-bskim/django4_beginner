from django.urls import path
from . import views

urlpatterns = [
    # 실제 url은 프로젝트 urls.py 에서 설정하므로 여기선 생략,
    # 생략한 부분을 추가하면, 프로젝트 path('first_app/') + 앱url path('simple_view') 로 구성된다.
    # domain.com/first_app/simple_view 로 구성됨,
    # view 인자는 실제 연결할 views의 함수 이름을 추가함,
    # path('', views.simple_view,),
    # path('sports/', views.sports_view,),
    # path('finance/', views.finance_view,),
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>', views.add_view),
]