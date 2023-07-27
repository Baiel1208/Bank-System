from django.contrib import admin

from transfers.models import HistoryTransfer

# Register your models here.
@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'is_completed', 'created_at', 'amount',)
    list_filter = ('is_completed', 'created_at',)
    search_fields = ('from_user__username', 'to_user__username',)