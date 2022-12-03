from django.urls import path
from . import views

urlpatterns = [
    path('test01data/', views.getTestDatas, name="test01data"),
    path('postMember/', views.postMember, name="postMember")
]