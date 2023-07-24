from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [("waiting", "waiting"), ("done", "done")]

    title = models.CharField(max_length=255)
    # waiting_time = models.PositiveSmallIntegerField(blank=True, null=True)
    waiting_time = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="waiting")

    def __str__(self) -> str:
        return "{}. {}: {}".format(self.id, self.title, self.status)
