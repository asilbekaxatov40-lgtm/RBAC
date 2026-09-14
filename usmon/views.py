from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import *
from utils.permissions import IsStudent, IsTeacher
from .serializers import *
from .models import Book

class BookCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BookSerializers

    def perform_create(self, serializer):
        serializers.save(owner=self.request.user)