from django.contrib import admin

from users.models import User, HistoryTransfer

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'created_at', 'age')
    list_filter = ('created_at', 'age')
    search_fields = ('username', 'email', 'phone_number')


@admin.register(HistoryTransfer)
class HistoryTransferAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'is_completed', 'created_at', 'amount')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('from_user__username', 'to_user__username')