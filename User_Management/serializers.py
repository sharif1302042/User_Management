from rest_framework import serializers

from User_Management.models import User


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username',)
