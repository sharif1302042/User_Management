from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

class GroupRequiredMixin(object):
    """
            group_required - list of strings, required param
        """
    group_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            raise PermissionDenied




