from django.db import models


class DNA_Extraction(models.Model):
    """
    Defines 'cook' protocol.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
