from django.urls import path
from . import views

urlpatterns = [
    path('test01datas/', views.getTestDatas, name="test01datas"),
]