from rest_framework import serializers
# from django.contrib.auth.models import User
# from ..users.models import MyUser
from ..users.models import *
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

# class RegisterSerializer(serializers.Serializer):
#     first_name=serializers.CharField()
#     last_name = serializers.CharField()
#     username=serializers.CharField()
#     password=serializers.CharField()
#
#     def validate(self, data):
#
#         if User.objects.filter(username=data['username']).exists():
#             raise serializers.ValidationError("Username already taken")
#         return data
#
#     def create(self, validated_data):
#         user = User.objects.create(first_name=validated_data['first_name'],
#                                    last_name=validated_data['last_name'],
#                                    username=validated_data['username'])
#         user.set_password(validated_data['password'])
#
#         return validated_data


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=12, min_length=8, write_only=True, required=True,
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']

    def validate(self, attrs):
        print("----------------", attrs)
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password: Password fields didn't match"})
        return super().validate(attrs)

    def validate_email(self, email):
        # email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email: Email already exists"})

        return super().validate(email)

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=50, required=True)
    password=serializers.CharField(max_length=50, required=True)

    class Meta:
        model = MyUser
        fields=['username', 'password']

    def validate(self, data):
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('account not found')
        return data

    def get_jwt_token(self, data):
        print("in here=================", data['username'], data['password'])
        user = authenticate(username = data['username'], password = data['password'])
        print("okay user", user)
        if not user:
            return {'message':"invalid credentials", "data":{}}

        refresh = RefreshToken.for_user(user)
        return {'message':"logged in successfully", "data":{'token':{
                                                                'refresh': str(refresh),
                                                                'access': str(refresh.access_token)}}}
