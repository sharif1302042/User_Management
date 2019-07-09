from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import permissions





class UserPermission(permissions.BasePermission):
    """
    If the permission method return True then granted otherwise it AccessDenied
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s', '%(app_label)s.change_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        print("permission Calling")
        if request.user.username=='sharif':
            return True
        return False

    # def has_object_permission(self, request, view, obj):
    #     print("Object Label Permission Calling")
    #     return True
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        #return obj.owner == request.user




