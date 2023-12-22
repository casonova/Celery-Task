# myproject/celery.py
from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("project")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "update-utc-times-every-5-minutes": {
        "task": "mainapp.tasks.update_customer_times",
        "schedule": timedelta(minutes=1),
    },
}
