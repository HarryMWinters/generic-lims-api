from django.db import models


class MasterMix(models.Model):
    """
    Defines mixture used in PCR reaction (in combination with tissue sample and dna extraction).
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
