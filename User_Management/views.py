from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#for assign group
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from User_Management.serializers import Userserializer
from .models import User

class UserCreation(APIView):
    def post(self,request):
        user = User.objects.create_user(username=request.data['username'],
                                                password=request.data['password']
                                                )
        if user:
            return Response('User Created Successfully',status = status.HTTP_201_CREATED)

        return Response('User Creation Failed',status = status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        users = User.objects.all()
        serializer = Userserializer(users, many=True)

        return Response(serializer.data,status = status.HTTP_200_OK)


class AssignUserToGroup(APIView):
    # content_type = ContentType.objects.get(app_label='myapp', model='BlogPost')
    # permission = Permission.objects.create(codename='can_publish',
    #                                        name='Can Publish Posts',
    #                                        content_type=content_type)


    def post(self,request):
        print(request.data)
        user = User.objects.get(username=request.data['username'])
        group = Group.objects.get(name=request.data['group'])
        a =user.groups.add(group)
        print(a)
        permissions = user.get_group_permissions()
        for p in permissions:
            print(p)

        if user.has_perm("User_Management.view_user"):
            print("Yes ")


        #print(group.name)

        return Response('Success',status = status.HTTP_200_OK)



