from django.db import models
from django.utils import timezone

class Csv(models.Model):
    file_name = models.FileField(upload_to='csvs/', max_length=100)
    uploaded = models.DateTimeField(default=timezone.now)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
