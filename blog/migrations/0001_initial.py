# Generated by Django 4.2.7 on 2023-11-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('date_of_publication', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
                'ordering': ('-date_of_publication',),
            },
        ),
    ]
