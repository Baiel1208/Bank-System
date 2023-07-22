from rest_framework import serializers
from .models import User, HistoryTransfer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'phone_number', 'created_at',
            'age', 'wallet_adress')


class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = (
            'id', 'from_user', 'to_user', 'is_completed', 'created_at',
            'amount' 
        )