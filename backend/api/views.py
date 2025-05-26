from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serlializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]