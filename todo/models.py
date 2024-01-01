from django.db import models
from django.utils import timezone
# Create your models here.

class todo(models.Model):
    task = models.CharField(max_length=256)
    status = models.CharField(max_length=50)
    createdat = models.DateTimeField('Created At')

    def __str__(self) -> str:
        return self.task + ' >> ' + self.status