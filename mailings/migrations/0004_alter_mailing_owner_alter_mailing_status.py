# Generated by Django 4.2.7 on 2023-11-12 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailings', '0003_mailing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('started', 'Запущена'), ('created', 'Создана'), ('done', 'Завершена')], default='created', max_length=20, verbose_name='статус рассылки'),
        ),
    ]