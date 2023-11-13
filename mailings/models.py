from django.conf import settings
from django.db import models


class Client(models.Model):
    email = models.EmailField(max_length=150, verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='комментарий',  null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', null=True)

    def __str__(self):
        return f'{self.full_name} - {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        

class Mailing(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'
    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'
    STATUSES = (
        (STATUS_STARTED, 'Запущена'),
        (STATUS_CREATED, 'Создана'),
        (STATUS_DONE, 'Завершена'),
    )

    start_time = models.TimeField(verbose_name='время начала рассылки')
    end_time = models.TimeField(verbose_name='время окончания рассылки')
    period = models.CharField(max_length=20, choices=PERIODS, verbose_name='периодичность рассылки')
    status = models.CharField(max_length=20, choices=STATUSES, default='created', verbose_name='статус рассылки')
    client = models.ManyToManyField('Client', verbose_name='клиент', related_name='client')
    title_message = models.CharField(max_length=150, verbose_name='тема письма')
    body_message = models.TextField(verbose_name='тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец', null=True)

    def __str__(self):
        return f'{self.start_time} - {self.end_time} ({self.period})'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('start_time',)


class Log(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    datetime = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус')
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='клиент')
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE, verbose_name='рассылка')
    error_msg = models.CharField(max_length=150,  null=True, blank=True, verbose_name='ответ почтового сервера')

    def __str__(self):
        return f'{self.datetime} - {self.status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
