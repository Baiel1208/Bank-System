from rest_framework import serializers
from django.contrib.auth import password_validation
from .models import User, HistoryTransfer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'phone_number', 'created_at',
            'age', 'wallet_adress')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name',
                'last_name', 'email', 'phone_number', 'created_at',
                'age', 'wallet_adress',)

# История переводов
class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = (
            'id', 'from_user', 'to_user', 'is_completed', 'created_at',
            'amount' 
        )

# Регистрация
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=30, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=30, write_only=True
    )

    class Meta:
        model = User
        fields = ('username','password', 'confirm_password')


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        if attrs['username'] == attrs['password']:
            raise serializers.ValidationError({'username':'Пароль похож на имя пользователя'})
        # Используйте функцию validate_password, чтобы применить все валидаторы пароля.
        password_validation.validate_password(attrs['password'], self.instance)
        return attrs