from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_staff']
        read_only_fields = ['is_staff']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
