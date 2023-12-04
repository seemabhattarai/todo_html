from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('login', LoginView, name="login"),
    path('register', UserRegisterView, name='register'),
    path('', Home, name="home"),
    path('detail/<str:pk>', TaskDetail, name="detail"),
    path('addtask', Addtask, name="addtask"),
    path('edittask/<str:pk>', EditTask, name= 'edittask'),
    path('deletetask/<str:pk>', DeleteTask, name= 'deletetask'),
]
