# Generated by Django 4.2.7 on 2023-11-05 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, verbose_name='почта')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='время начала рассылки')),
                ('end_time', models.TimeField(verbose_name='время окончания рассылки')),
                ('period', models.CharField(choices=[('daily', 'Ежедневная'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=20, verbose_name='периодичность рассылки')),
                ('status', models.CharField(choices=[('started', 'Запущена'), ('created', 'Создана'), ('done', 'Завершена')], max_length=20, verbose_name='статус рассылки')),
                ('title_message', models.CharField(max_length=150, verbose_name='тема письма')),
                ('body_message', models.TextField(verbose_name='тело письма')),
                ('client', models.ManyToManyField(to='mailings.client', verbose_name='клиент')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='дата и время последней попытки')),
                ('status', models.CharField(choices=[('ok', 'Успешно'), ('failed', 'Ошибка')], max_length=20, verbose_name='статус')),
                ('error_msg', models.CharField(max_length=150, verbose_name='ответ почтового сервера')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.client', verbose_name='клиент')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailing', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
            },
        ),
    ]
