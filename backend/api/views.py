from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from .ml_models import Job_Prediction
from dotenv import load_dotenv
import os

load_dotenv()

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

class AdminVerify(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return Response({
                'status': True,
                'message': 'Welcome Admin'
            }, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'status': False,
                'message': 'Imposter Alert'
            }, status=status.HTTP_403_FORBIDDEN)
# Authentication Views
class UserRegisterApi(APIView):
    permission_classes=[AllowAny]
    
    def post(self, request):
        user_serializer = UserSerializer(data={
            'username': request.data.get('username'),
            'password': request.data.get('password')
        })
        
        if not user_serializer.is_valid():
            return Response({
                "status": False,
                "errors": user_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = user_serializer.save()
        
        profile_data = {
            'user': user.id,
            'full_name': request.data.get('full_name'),
            'email': request.data.get('email'),
            'mobile': request.data.get('mobile'),
            'dob': request.data.get('dob'),
            'user_type': request.data.get('user_type')
        }
        
        profile_serializer = UserRegisterSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response({
                "status": True,
                "message": "User registered successfully",
                "user": user_serializer.data,
                "profile": profile_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response({
                "status": False,
                "errors": profile_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_csrf_token(request):
    return Response({'csrfToken': get_token(request)})

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({
            'detail': 'Login successful',
            'username': user.username
        })
    return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class Rform(generics.CreateAPIView):
    @permission_classes([AllowAny])

    def post(self, request, *args, **kwargs):
        prediction=Job_Prediction(request.data)
        return Response({
            "status": True,
            "message": f"{prediction.predict()}"
        }, status=status.HTTP_200_OK)