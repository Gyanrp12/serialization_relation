from django.shortcuts import render
from .models import Author, Book
from rest_framework import viewsets
from .serializers import AuthorSer,BookSer

# Create your views here.



class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSer
    
    
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSer