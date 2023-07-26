from django.urls import path

from .views import CreateTransfersView, MoneyTransferHistoryView

urlpatterns = [
    path('transfers/', CreateTransfersView.as_view(), name="transfers"),
    path('money/transfer/history/', MoneyTransferHistoryView.as_view(), name='money_transfer_history'),
]