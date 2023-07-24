from datetime import timedelta
from random import randint

from celery import shared_task
from django.utils import timezone

from tasks.models import Task


@shared_task
def add_waiting_time_to_task(id):
    print("ADD_WAITING_TIME_TO_TASK")
    task = Task.objects.get(id=id)
    task.waiting_time = timezone.now() + timedelta(minutes=randint(1, 10))
    task.save()


@shared_task
def update_status_if_waiting_time_is_expired():
    Task.objects.filter(waiting_time__lte=timezone.now()).update(status="done")
    print("UPDATE_STATUS_IF_WAITING_TIME_IS_EXPIRED")
