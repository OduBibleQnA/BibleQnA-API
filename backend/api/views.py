from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serlializers import UserSerializer, QuestionSerializer, TestimonySerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Question, Testimony


class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class CreateQuestion(generics.CreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    http_method_names = ["post"]


class TestimonyListCreate(generics.ListCreateAPIView):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class CreateTestimony(generics.CreateAPIView):
    serializer_class = TestimonySerializer
    permission_classes = [AllowAny]

    http_method_names = ["post"]


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
