from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,  name = "home"),
    path('api/contact/', views.ContactMessageCreateView.as_view(), name='contact-message-create'),

]