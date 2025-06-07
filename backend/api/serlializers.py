from cryptography.fernet import Fernet
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import serializers
from .models import Question, Testimony

cipher = Fernet(settings.ENCRYPTION_KEY)

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

    def validate_contact_detail(self, value):
        if not value:
            raise serializers.ValidationError("Contact detail must be included")
        return value

    def create(self, validated_data):
        contact_detail = validated_data.get('contact_detail')
        if contact_detail:
            encrypted_contact_detail = cipher.encrypt(contact_detail.encode("utf-8"))
            validated_data['contact_detail'] = encrypted_contact_detail
        
        return super().create(validated_data)