from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def home(request:Request):

    if request.method == 'POST':
        data=request.data
        response = {'message':'Hello world, POST',"data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)
    
    response = {'message':'Hello world, GET'}
    return Response(data=response,status=status.HTTP_200_OK)