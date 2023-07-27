from rest_framework import serializers

from transfers.models import HistoryTransfer


# История переводов
class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = (
            'id', 'from_user', 'to_user', 'is_completed', 'created_at',
            'amount' 
        )

class MoneyTransferHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        # fields = ('id', )
        fields = (
            'id', 'from_user', 'to_user', 'is_completed', 'created_at',
            'amount' 
        )