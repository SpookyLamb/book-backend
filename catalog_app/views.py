from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets

from .models import *
from .serializers import *

    # 'GET',
    # 'POST',
    # 'PUT',
    # 'PATCH',
    # 'DELETE',
    # 'OPTIONS',

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@api_view(['GET'])
def get_profile(request):
    user = request.user
    profile = user.profile
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)

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

#book create (post)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_book(request):
    user = request.user

    book = Book.objects.create(
        user = user,
        title = request.data['title'],
        author = request.data['author'],
        genre = request.data['genre'],
        favorite = request.data['favorite'],
        user_rating = request.data['user_rating'],
    )
    book.save()
    
    book_serialized = BookSerializer(book)
    return Response(book_serialized.data)

#book read (get)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    #grab all the books attached to a given user
    user = request.user
    books = user.book_set.all() #related name - https://docs.djangoproject.com/en/stable/topics/db/queries/#backwards-related-objects
    books_serialized = {}

    for book in books:
        book_serialized = BookSerializer(book)
        books_serialized[str(book_serialized.data["id"])] = book_serialized.data

    return Response(books_serialized)

#book update (put)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_book(request):
    id = request.data['id']

    #grab the book with the specific id
    book = Book.objects.get(pk=id)

    book.title = request.data['title']
    book.author = request.data['author']
    book.genre = request.data['genre']
    book.favorite = request.data['favorite']
    book.user_rating = request.data['user_rating']
    book.save()
    
    book_serialized = BookSerializer(book)
    return Response(book_serialized.data)

#book delete (delete)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(request):
    id = request.data['id']

    #grab the book with the specific id
    book = Book.objects.get(pk=id)
    book.delete()
    
    return Response()