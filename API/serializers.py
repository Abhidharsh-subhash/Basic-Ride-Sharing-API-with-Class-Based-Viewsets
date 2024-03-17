import re
from rest_framework import serializers
from .models import Users
from django.db.models import Q
from django.core.validators import EmailValidator
from django.contrib.auth import authenticate

class UserSignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ('username', 'email', 'phone_number', 'password', 'confirm_password')

    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")

        # Validate email format using regex
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
            raise serializers.ValidationError("Invalid email format")

        if not re.match(r'^[789]\d{9}$', data['phone_number']):
            raise serializers.ValidationError("Invalid phone number format")

        if not re.match(r'^[a-zA-Z]{3,15}$', data['username']):
            raise serializers.ValidationError("Invalid username format")
        
        if Users.objects.filter(email=data['email'],is_user=True).exists():
            raise serializers.ValidationError('User with the Email already exist')
        
        if Users.objects.filter(phone_number=data['phone_number'],is_user=True).exists():
            raise serializers.ValidationError('User with the phone number already exist')

        return data

    def create(self, validated_data):
        user = Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            is_user=True
        )
        return user

class DriverSignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ('username', 'email', 'phone_number', 'password', 'confirm_password')

    def validate(self, data):
        if data['password'] != data.pop('confirm_password'):
            raise serializers.ValidationError("Passwords do not match")

        # Validate email format using regex
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
            raise serializers.ValidationError("Invalid email format")

        if not re.match(r'^[789]\d{9}$', data['phone_number']):
            raise serializers.ValidationError("Invalid phone number format")

        if not re.match(r'^[a-zA-Z]{3,15}$', data['username']):
            raise serializers.ValidationError("Invalid username format")
        
        if Users.objects.filter(email=data['email'],is_staff=True).exists():
            raise serializers.ValidationError('Driver with the Email already exist')
        
        if Users.objects.filter(phone_number=data['phone_number'],is_staff=True).exists():
            raise serializers.ValidationError('Driver with the phone number already exist')

        return data

    def create(self, validated_data):
        user = Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            is_staff=True
        )
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(validators=[EmailValidator()])
    password=serializers.CharField(style={'input-type':'password'})
    class Meta:
        model=Users
        fields=['email','password']
    def validate(self, attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        if email and password:
            user=authenticate(email=email,password=password)
            if user:
                if user.is_user == False:
                    raise serializers.ValidationError('Invalid Credentials')
                else:
                    attrs['user']=user
            else:
                raise serializers.ValidationError('Invalid Credentials')
        else:
            raise serializers.ValidationError('Email and Password are required')
        return attrs
    
class DriverLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(validators=[EmailValidator()])
    password=serializers.CharField(style={'input-type':'password'})
    class Meta:
        model=Users
        fields=['email','password']
    def validate(self, attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        if email and password:
            user=authenticate(email=email,password=password)
            if user:
                if user.is_staff == False:
                    raise serializers.ValidationError('Invalid Credentials')
                else:
                    attrs['user']=user
            else:
                raise serializers.ValidationError('Invalid Credentials')
        else:
            raise serializers.ValidationError('Email and Password are required')
        return attrs