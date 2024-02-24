from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name="main_home" ),
    path('contact.html/', views.contact, name='contact.html'),

]