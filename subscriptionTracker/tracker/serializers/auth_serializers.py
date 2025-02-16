from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "full_name"]
        
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        user = User.create(**validated_data)
        return user
        
    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "user": {
                "id": instance.id,
                "username": instance.username,
                "email": insecure.email,
                "full_name": instance.full_name,
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        