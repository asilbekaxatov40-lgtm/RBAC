from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# local
from .models import *
from .serializers import *

class RegisterApiView(APIView):
    permission_classes = [AllowAny]
    serializers_class = RegisterSerializers
    @extend_schema(request=RegisterSerializers)
    def post(self, request):
        serializers = self.serializers_class(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response({'message': 'User yaraldi', 'user_id': user.id})
        return Response(serializers.errors)

class LoginApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializers
    @extend_schema(request=LoginSerializers)
    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            username = serializers.validated_data.get('username')
            password = serializers.validated_data.get('password')

            user = authenticate(username=username, password=password)
            refresh = RefreshToken.for_user(user)
            if user:
                return Response({'messages': 'User login buldi', 'access': str(refresh.access_token), 'refresh': str(refresh)})
            return Response(serializers.errors)