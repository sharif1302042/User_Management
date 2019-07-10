from django.contrib.auth.models import Group

from User_Management.models import User

def is_member(requested_data):
    try:
        # user = User.objects.get(username=requested_data['username']).groups.all()
        # group = Group.objects.get(name=requested_data['group'])

        return User.objects.filter(username=requested_data['username'],
                            groups__name=requested_data['group']).exists()

    except Exception as err:
        print(err)
        return False

def is_member_of_multiple_groups(requested_data):
    try:
        user = User.objects.get(username=requested_data['username'])
        groups = Group.objects.all()
        print(groups)
        users_in_group = Group.objects.get(name="visitor").user_set.all()
        # for check all userlist in this group
        print(users_in_group)
        if user in users_in_group:
            return True

    except Exception as err:
        print(err)
        return False






