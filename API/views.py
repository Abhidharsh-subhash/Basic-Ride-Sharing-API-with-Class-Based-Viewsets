from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import Users
from . import serializers

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
    
class RiderSignupViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = serializers.RiderSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Rider registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
