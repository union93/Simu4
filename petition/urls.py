from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('list/', views.petition_list, name="list"),
    path('write/', views.petition_write, name="write"),
]