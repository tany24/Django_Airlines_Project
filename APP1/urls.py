from django.urls import path
from APP1 import views

urlpatterns = [
    path('',views.index,name="index"),
    path('original_index',views.originl_index,name='previous-index'),
    path('help',views.help,name="HELP"),
]
