from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.core.management import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from mailings.models import Mailing, Log
import logging
from mailings.services import send_mailings

logger = logging.getLogger(__name__)


def my_job():
    now = datetime.now()
    mailings = Mailing.objects.exclude(status='done')
    for mailing in mailings:
        clients = mailing.client.all()
        for client in clients:
            log = Log.objects.filter(client=client, mailing=mailing).last()
            if log is not None:
                if mailing.period == 'daily':
                    delta = timedelta(days=1)
                    date_send = log.datetime + delta
                    if date_send.date() <= now.date() and mailing.start_time <= now.time() <= mailing.end_time:
                        send_mailings(mailing, client)
                        Log.objects.create(datetime=now, status='ok', client=client, mailing=mailing,
                                           error_msg='error_msg')
                elif mailing.period == 'weekly':
                    delta = timedelta(days=7)
                    date_send = log.datetime + delta
                    if date_send.date() <= now.date() and mailing.start_time < now.time() < mailing.end_time:
                        send_mailings(mailing, client)
                        Log.objects.create(datetime=now, status='ok', client=client, mailing=mailing,
                                           error_msg='error_msg')
                elif mailing.period == 'monthly':
                    delta = timedelta(days=30)
                    date_send = log.datetime + delta
                    if date_send.date() <= now.date() and mailing.start_time < now.time() < mailing.end_time:
                        send_mailings(mailing, client)
                        Log.objects.create(datetime=now, status='ok', client=client, mailing=mailing,
                                           error_msg='error_msg')
            else:
                if mailing.start_time < now.time() < mailing.end_time:
                    error_msg, status = send_mailings(mailing, client)
                    Log.objects.create(datetime=now, status=status, client=client, mailing=mailing, error_msg=error_msg)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(my_job,
                          trigger=CronTrigger(minute='*/5'),
                          id='my_job', max_instances=1,
                          replace_existing=True
                          )
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            logger.info('scheduler остановился')
            scheduler.shutdown()


