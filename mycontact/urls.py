from django import views
from django.urls import path
from .views import ContactFormView 
from . import views

urlpatterns = [
    path('home/' , views.index , name='home'),
    path('contact/' , ContactFormView.as_view()  ,name='contactform'), 
]