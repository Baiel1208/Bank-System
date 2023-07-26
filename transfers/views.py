from rest_framework.generics import CreateAPIView, ListAPIView

from transfers.serializers import HistoryTransferSerializer

# Create your views here.
class CreateTransfersView(CreateAPIView):
    serializer_class = HistoryTransferSerializer



class MoneyTransferHistoryView(ListAPIView):
    serializer_class = HistoryTransferSerializer
    