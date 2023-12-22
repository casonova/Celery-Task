import logging
import os

import pytz
from celery import shared_task

from mainapp.models import Customer
from project.settings import BASE_DIR

logger = logging.getLogger(__name__)


@shared_task
def update_customer_times():
    records_fetch = 10
    count = read_count()

    if Customer.objects.filter(is_utc=False).count() == count and count < 100:
        fetched_records = Customer.objects.filter(is_utc=True)[:records_fetch]
        for record in fetched_records:
            utc_time = record.Time
            pst_time = utc_time.astimezone(pytz.timezone("Asia/Karachi"))
            record.Time = pst_time
            record.is_utc = False
            record.is_pst = True
            record.save()
            logger.info(
                f"Customer {record.id} time in utc format {utc_time} is updated in pst format {record.Time}"
            )
        update_count(count)

    elif Customer.objects.filter(is_pst=False).count() == count and count < 100:
        fetched_records = Customer.objects.filter(is_pst=True)[:records_fetch]
        for record in fetched_records:
            pst_time = record.Time
            utc_time = pst_time.astimezone(pytz.utc)
            record.Time = utc_time
            record.is_utc = True
            record.is_pst = False
            record.save()
            logger.info(
                f"Customer {record.id} time in pst_format {pst_time} is updated in utc format {record.Time}"
            )
        update_count(count)
    elif count == 100:
        count = 0
        iteration_file_path = os.path.join(BASE_DIR, "CountIteration.txt")
        with open(iteration_file_path, "w") as f:
            f.write(str(count))


def read_count():
    iteration_file_path = os.path.join(BASE_DIR, "CountIteration.txt")
    with open(iteration_file_path, "r") as f:
        return int(f.read())


def update_count(count):
    iteration_file_path = os.path.join(BASE_DIR, "CountIteration.txt")

    if count < 100:
        count += 10
    with open(iteration_file_path, "w") as f:
        f.write(str(count))