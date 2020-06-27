from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'confirm_password',)


class PasswordChangeSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['old_password', 'new_password']
