from django.db import models


class GelImage(models.Model):
    """
    Defines gel image (and positive lanes etc.) from an successful electrophoresis run.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
