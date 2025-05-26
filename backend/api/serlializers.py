from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question, Testimony


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            "id",
            "first_name",
            "question",
            "submitted_at",
            "answered",
            "answer_medium",
            "answer_date",
            "archived",
        ]

    def create(self, validated_data):
        question = Question.objects.create(**validated_data)
        return question


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = [
            "name",
            "shortened_testimony",
            "on_camera",
            "contact_method",
            "contact_detail",
            "approved",
            "archived",
            "submitted_at",
        ]

    def create(self, validated_data):
        testimony = Testimony.objects.create(**validated_data)
        return testimony
