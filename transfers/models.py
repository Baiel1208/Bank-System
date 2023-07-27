from django.db import models

from users.models import User

# Create your models here.
# История перевода денег
class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_transfers", 
        verbose_name="От кого"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_transfers',
        verbose_name="Кому"
    )
    is_completed = models.BooleanField(default=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Количество')


    def __str__(self) -> str:
        return self.amount 
        # return f'Перевод от {self.from_user} к {self.to_user}'


    class Meta:
        verbose_name = "История переводов"
        verbose_name_plural = "История переводов"