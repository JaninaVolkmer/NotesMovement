from django.db import models
from django.utils import timezone
# Create your models here.
"""
Create fields:
:title:         headline
:notes:       main text body
:date_created:  creation date + time
"""


class Entry(models.Model):
    title = models.CharField(max_length=200)
    notes = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    # customize title as string representation
    def __str__(self):
        return self.title

    # Plural name for the object:
    class Meta:
        verbose_name_plural = "Entries"
