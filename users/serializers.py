from rest_framework import serializers
from .models import User, Address

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "phone",
            "full_name",
            "email",
            "password"
        ]

    def create(self,validated_data):
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "full_name",
            "email",
            "role",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "phone",
            "role",
            "created_at",
        ]


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            "id",
            "title",
            "latitude",
            "longitude",
            "full_address",
        ]
        read_only_fields = ["id"]
        
        
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "phone",
            "full_name",
            "email",
            "role",
            "created_at",
        ]
        read_only_fields = fields
        
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'full_name', 'email']
        
        
class EmployeeCreateSerializer(serializers.Serializer):
    phone = serializers.CharField()
    role = serializers.ChoiceField(
        choices=["courier","operator"]
    )
    
    