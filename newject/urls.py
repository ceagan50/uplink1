from django.urls import path
from .import  views

urlpatterns = [
    path('', views.home, name='home'),  # This handles the root URL (http://127.0.0.1:8000/)
    path('sermons/', views.sermons, name='sermons'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('accounts/logout/', views.admin_logout, name='admin_logout'),
  
]
