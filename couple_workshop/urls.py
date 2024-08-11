from django.urls import path
from . import views

urlpatterns = [
    path('', views.couples_work_shop,  name = "home"),

]