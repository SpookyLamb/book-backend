from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def get_profile(request):
    user = request.user
    profile = user.profile
    serialized_profile = ProfileSerializer(profile)
    return Response(serialized_profile.data)

@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
    )
    user.set_password(request.data['password'])
    user.save()
    
    profile = Profile.objects.create(
        user = user,
        email = request.data['email'],
        first_name = request.data['first_name'],
        last_name = request.data['last_name'],
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)