from rest_framework import serializers
from django.contrib.auth import User
class RegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, data):

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already taken")
        return data
