from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
   class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Add more fields as needed
        extra_kwargs = {'password': {'write_only': True}}

   def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user