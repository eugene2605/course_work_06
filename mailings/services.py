from smtplib import SMTPServerDisconnected, SMTPSenderRefused, SMTPRecipientsRefused, SMTPDataError, SMTPConnectError, \
    SMTPNotSupportedError, SMTPAuthenticationError

from django.conf import settings
from django.core.mail import send_mail


def send_mailings(mailing, client):

    try:
        send_mail(
            mailing.title_message,
            mailing.body_message,
            settings.EMAIL_HOST_USER,
            [client.email],
            fail_silently=False
        )
    except SMTPServerDisconnected:
        error_msg = 'SMTPServerDisconnected - сервер отключился'
        status = 'failed'
    except SMTPSenderRefused:
        error_msg = 'SMTPSenderRefused - адрес отправителя отклонен'
        status = 'failed'
    except SMTPRecipientsRefused:
        error_msg = 'SMTPRecipientsRefused - все адреса получателей отказались'
        status = 'failed'
    except SMTPDataError:
        error_msg = 'SMTPDataError - SMTP-сервер отказался принять данные сообщения'
        status = 'failed'
    except SMTPConnectError:
        error_msg = 'SMTPConnectError - произошла ошибка при установлении соединения с сервером'
        status = 'failed'
    except SMTPNotSupportedError:
        error_msg = 'SMTPNotSupportedError - использованная команда или параметр не поддерживается сервером'
        status = 'failed'
    except SMTPAuthenticationError:
        error_msg = 'SMTPAuthenticationError - аутентификация SMTP прошла неправильно'
        status = 'failed'
    except:
        error_msg = 'Прочая ошибка'
        status = 'failed'
    else:
        error_msg = 'Ошибки отсутствуют'
        status = 'ok'

    return error_msg, status
