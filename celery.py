from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from library.models import Book
from datetime import datetime, timedelta
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('librarysystem')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 30 seconds.
    sender.add_periodic_task(30.0, archive('hello'), name='add every 30 seconds')

@app.task(bind=True)
def archive(self):
    ten_years_ago = timezone.now() - timedelta(days=10 * 365)
    records = Book.objects.filter(published_date__lte=ten_years_ago).update(is_archived=True)

