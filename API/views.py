from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets

# Create your views here.


@api_view(['GET', 'POST'])
def home(request: Request):

    if request.method == 'POST':
        data = request.data
        response = {'message': 'Hello world, POST', "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {'message': 'Hello world, GET'}
    return Response(data=response, status=status.HTTP_200_OK)


class sample(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        return Response({"message": "it is a POST method"}, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return Response({"message": "it is a GET method"}, status=status.HTTP_200_OK)
