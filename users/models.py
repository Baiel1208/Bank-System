import random, string
from django.db import models

from django.contrib.auth.models import AbstractUser


def generate_wallet_address():
    # Генерируем случайную строку из 12 символов (цифры и буквы в верхнем и нижнем регистре)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))



# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=16 ,unique=True, verbose_name="Номер телефона"
    )
    age = models.PositiveIntegerField(blank=True,null=True,
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
