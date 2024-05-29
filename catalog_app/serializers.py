from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' #["id", "username", "password"]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__' #["id", "email" "first_name", "last_name"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'