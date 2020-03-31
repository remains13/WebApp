from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ServerSerializer 
from .models import Server


class ServerView(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    queryset = Server.objects.all()
