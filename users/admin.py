from django.contrib import admin

from users.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'created_at', 'age')
    list_filter = ('created_at', 'age')
    search_fields = ('username', 'email', 'phone_number')
