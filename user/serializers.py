from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','username', 'password']
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
