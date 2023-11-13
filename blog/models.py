from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='изображение')
    date_of_publication = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='дата публикации')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.date_of_publication}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('-date_of_publication',)
