from rest_framework import serializers
from django.contrib.auth import password_validation
from .models import User

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


# Регистрация
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    confirm_password = serializers.CharField(
        max_length=255, write_only=True
    )

    class Meta:
        model = User
        fields = ('id',  'username', 'email', 
                'phone_number', 'age','created_at','password', 'confirm_password')


    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        if attrs['username'] == attrs['password']:
            raise serializers.ValidationError({'username':'Пароль похож на имя пользователя'})
        # Используйте функцию validate_password, чтобы применить все валидаторы пароля.
        password_validation.validate_password(attrs['password'], self.instance)
        # phone number 
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError('Номер телефона должен быть в формате +996*********')
        return attrs


    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

