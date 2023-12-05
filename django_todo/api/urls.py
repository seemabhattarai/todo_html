from django.urls import path
from .views import *
from .import views

urlpatterns = [
    path('home', HomeView.as_view(), name="homeview"),

]