from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from . import serializers
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from .import models
from .import permissions

class sample(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        return Response({"message": "it is a POST method"}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return Response({"message": "it is a GET method"}, status=status.HTTP_200_OK)
    
class UserSignupViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DriverSignupViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.DriverSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Driver registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginViewSet(viewsets.ViewSet):
    serializer_class = serializers.UserLoginSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = RefreshToken.for_user(user)
        response = {
            'message': 'User logged in successfully',
            'access': str(tokens.access_token),
            'refresh': str(tokens)
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
class DriverLoginViewSet(viewsets.ViewSet):
    serializer_class = serializers.DriverLoginSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        tokens = RefreshToken.for_user(user)
        response = {
            'message': 'Driver logged in successfully',
            'access': str(tokens.access_token),
            'refresh': str(tokens)
        }
        return Response(data=response, status=status.HTTP_200_OK)

class DriverList(viewsets.ViewSet):
    permission_classes = [permissions.IsUser]
    def list(self,request):
        drivers = models.Users.objects.filter(is_staff=True).all()
        serializer = serializers.DriverListSerializer(instance=drivers,many=True)
        return Response(serializer.data)