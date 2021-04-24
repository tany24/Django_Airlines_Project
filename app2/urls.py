from django.urls import path, include
from app2 import views

urlpatterns = [
    path('',views.userList,name='User List'),
]
