from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile
import re


class ProfileCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "password", "email", "bio"]

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "The password must have at least 8 characters."
            )

        if not re.search(r"[#@%&!]", value):
            raise serializers.ValidationError(
                "Password must contain at least one special character."
            )

        return value

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))

        return super(ProfileCreationSerializer, self).create(validated_data)
