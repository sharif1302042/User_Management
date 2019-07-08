from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

class UserCreation(APIView):
    def post(self,request):
        user = User.objects.create_user(username=request.data['username'],
                                                password=request.data['password']
                                                )
        if user:
            return Response('User Created Successfully',status = status.HTTP_201_CREATED)

        return Response('User Creation Failed',status = status.HTTP_400_BAD_REQUEST)
