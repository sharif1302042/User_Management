from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# for assign group
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from User_Management.serializers import Userserializer
from .models import User
from .mixins import GroupRequiredMixin
from applibs.check_user_group import is_member, is_member_of_multiple_groups


class UserCreation(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.data['username'],
                                        password=request.data['password']
                                        )
        if user:
            return Response('User Created Successfully', status=status.HTTP_201_CREATED)
        return Response('User Creation Failed', status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = User.objects.all()
        serializer = Userserializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AssignUserToGroup(APIView):
    # content_type = ContentType.objects.get(app_label='myapp', model='BlogPost')
    # permission = Permission.objects.create(codename='can_publish',
    #                                        name='Can Publish Posts',
    #                                        content_type=content_type)

    def post(self, request):
        try:
            # print("group_name",request.user.groups.all())
            user = User.objects.get(username=request.data['username'])
            group = Group.objects.get(name=request.data['group'])
            # user = User.objects.get(username=request.data['username']).groups.all()

            user.groups.add(group)

            # permissions = user.get_group_permissions()
            # for p in permissions:
            #     print(p)
            #
            # if user.has_perm("User_Management.view_user"):
            #     print("Yes ")

            return Response('Successfully Added The User to Group', status=status.HTTP_201_CREATED)
        except Exception as err:
            print(err)
            return Response('Failed to Assigned User to Group', status=status.HTTP_400_BAD_REQUEST)


class CheckUserGroup(APIView):
    def post(self, request):
        if not is_member_of_multiple_groups(request.data):
            return Response('Access Denied', status=status.HTTP_403_FORBIDDEN)
        return Response('Request Granted', status=status.HTTP_200_OK)


class RemoveUserFromGroup(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.data['username'])
            user.groups.clear()
            return Response('Successfully Remove The User From Group', status=status.HTTP_200_OK)
        except Exception as err:
            return Response('Failed to Remove User From Group', status=status.HTTP_400_BAD_REQUEST)
