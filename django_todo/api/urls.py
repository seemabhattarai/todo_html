from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('home', HomeView.as_view(), name="homeview"),
    path('task/<str:pk>', UpdateTask.as_view() , name= 'task'),

]