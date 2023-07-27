from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status

from transfers.models import HistoryTransfer
from transfers.serializers import HistoryTransferSerializer
from users.models import User

# Create your views here.
class CreateTransfersView(CreateAPIView):
    serializer_class = HistoryTransferSerializer
    permission_classes = [IsAuthenticated]


    def post(self, request):
        from_user_id = request.data.get('from_user')
        to_user_id = request.data.get('to_user')
        amount = request.data.get('amount')
        try:
            from_user = User.objects.get(id=from_user_id)
            to_user = User.objects.get(id=to_user_id)
            if float(amount) > float(from_user.balance):
                return Response({'detail': 'Недостаточно средств для перевода'}, status=status.HTTP_400_BAD_REQUEST)
            from_user.balance = float(from_user.balance) - float(amount)
            to_user.balance = float(to_user.balance) + float(amount)
            from_user.save()
            to_user.save()
            transfer = HistoryTransfer.objects.create(from_user=from_user, to_user=to_user, amount=amount)
            serializer = HistoryTransferSerializer(transfer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'detail': 'Неверный формат суммы перевода'}, status=status.HTTP_400_BAD_REQUEST)


    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)



# History
class MoneyTransferHistoryView(ListAPIView):
    serializer_class = HistoryTransferSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return HistoryTransfer.objects.filter(Q(from_user=user) | Q(to_user=user))