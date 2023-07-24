from django.db import models


class Task(models.Model):
    DONE = "DO"
    WAITING = "WA"
    STATUS_CHOICES = [(WAITING, "waiting"), (DONE, "done")]

    title = models.CharField(max_length=255)
    waiting_time = models.PositiveSmallIntegerField(blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
