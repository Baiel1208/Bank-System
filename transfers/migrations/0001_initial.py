# Generated by Django 4.2.3 on 2023-07-26 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_delete_historytransfer'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Количество')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_transfers', to='users.user', verbose_name='От кого')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_transfers', to='users.user', verbose_name='Кому')),
            ],
            options={
                'verbose_name': 'История переводов',
                'verbose_name_plural': 'История переводов',
            },
        ),
    ]
