from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAuthenticatedUser
from .models import Address

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ProfileSerializer,
    ProfileUpdateSerializer,
    AddressSerializer
)


@extend_schema(
    tags=['Authentication'],
    request=RegisterSerializer,
    responses=RegisterSerializer
)
class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()  

            return Response(
                {
                    "message": "Foydalanuvchi muvaffaqiyatli ro'yxatdan o'tdi",
                    "user_id": user.id,
                    "phone": user.phone,
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@extend_schema(
    tags=['Authentication'],
    request=LoginSerializer,
    responses=LoginSerializer
)

class LoginView(APIView):
    
    def post(self,request):
        
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']
            
            user = authenticate(
                request, 
                phone=phone, 
                password=password
                )
            
            if user is None:
                return Response(
                    {"detail": "Telefon raqam yoki parol noto'g'ri"},
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
            refresh  = RefreshToken.for_user(user)
            
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "role": user.role,
                },
                status=status.HTTP_200_OK   
            )
            
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@extend_schema(
    tags=['Profile'],
    responses=ProfileSerializer,
    request=ProfileUpdateSerializer
)
class ProfileView(APIView):
    permission_classes = [IsAuthenticatedUser]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
    
    def patch(self,request):
        serializer = ProfileUpdateSerializer(request.user, data=request.data, partial=True)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
@extend_schema(
    tags=['Address'],
    responses=AddressSerializer,
    request=AddressSerializer
)
class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    






    
    


