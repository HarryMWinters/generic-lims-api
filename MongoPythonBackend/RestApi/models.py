from django.db import models


class Assay(models.Model):
    record_timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['record_timestamp']
