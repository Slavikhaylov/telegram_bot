from django.db import models
from django.conf import settings
from django.utils import timezone


class StatusCode(models.Model):
    status_code = models.SmallIntegerField(blank=True, null=True)
    date_created = models.DateTimeField('Дата и время', default=timezone.now)

    def __str__(self) -> str:
        return str(self.status_code)



