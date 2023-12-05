from django.shortcuts import render
from todoapp.models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response


class HomeView(APIView):
    def get (get, request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)


# Create your views here.
