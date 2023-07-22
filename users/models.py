import random, string
from django.db import models


def generate_wallet_address():
    # Генерируем случайную строку из 12 символов (цифры и буквы в верхнем и нижнем регистре)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))



# Create your models here.
class User(models.Model):
    username = models.CharField(
        max_length=255,verbose_name="Имя пользователя", unique=True
    ) 
    email = models.EmailField(
        verbose_name="Адрес электронной почты", unique=True
    )
    phone_number = models.CharField(
        max_length=16 ,unique=True, verbose_name="Номер телефона"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата и время входа'
    )
    age = models.PositiveIntegerField(
        verbose_name="Возраст"
    )
    balance = models.CharField(
        max_length=255,
        verbose_name="Баланс",
        blank = True, null = True,
        default=0
    )
    wallet_adress = models.CharField(
        max_length=12, default=generate_wallet_address,
        verbose_name='Уникальный кошелек'
    )

    def __str__(self):
        return self.username


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



# История перевода денег
class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name="sent_transfers", 
        verbose_name="От кого"
    )
    to_user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='received_transfers',
        verbose_name="Кому"
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self) -> str:
        return f'Перевод от {self.from_user} к {self.to_user}'


    class Meta:
        verbose_name = "История переводов"
        verbose_name_plural = "История переводов"