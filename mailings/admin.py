from django.contrib import admin

from mailings.models import Client, Mailing, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment')
    list_filter = ('email',)
    search_fields = ('email', 'full_name')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_time', 'end_time', 'period', 'status', 'title_message', 'body_message')
    list_filter = ('start_time', 'end_time', 'period', 'status')
    search_fields = ('period', 'status')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime', 'status', 'client', 'mailing', 'error_msg')
    list_filter = ('status', 'client', 'mailing')
    search_fields = ('status', 'client', 'mailing')
