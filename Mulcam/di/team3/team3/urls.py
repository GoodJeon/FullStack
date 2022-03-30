"""accident URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 인덱스 페이지
    path('',views.index),

    # 인프라 페이지
    path('infra/',views.infra),
    path('infra/infra_data/',views.infra_data),
    path('infra/all_infra/',views.all_infra),
    path('infra/sago_data/',views.sago_data,name='sago_data'),
    path('infra/infPopulation_data/', views.infPopulation_data),
    
    # 키워드 카테고리 페이지
    path('infra/keyword/', views.keyword),
    path('infra/keyword/keyword_data/', views.keyword_data),
    
    # 전국 사고다발지역 파이차트 페이지
    path('infra/keyword/pie/', views.pie),
    path('infra/keyword/pie/sido_pie/',views.sido_pie),

]
