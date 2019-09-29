from django.db import models


class TissueSample(models.Model):
    """
    Defines pre DNA extraction sample.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
