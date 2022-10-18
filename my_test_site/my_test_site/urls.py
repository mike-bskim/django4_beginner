"""my_test_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 직접호출하는 경우
from my_app import views

urlpatterns = [
    # 직접호출하는 경우
    path('my_app/', views.index, ),

    # 간접호출하는 경우, Including another URLconf
    # path('my_app/', include('my_app.urls')), # 추가한 app 을 등록해야 한다
    path('admin/', admin.site.urls),
]
