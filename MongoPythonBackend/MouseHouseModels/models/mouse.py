from django.db import models


class Mouse(models.Model):
    """
    Define murine model for genotyping.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
