from django.db import models
from .researcher import Researcher


class MasterMix(models.Model):
    """
    Defines mixture used in PCR reaction (in combination with tissue sample and dna extraction).
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=False, auto_created=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        Researcher, on_delete=models.PROTECT)
    primers = models.TextField(null=False)
