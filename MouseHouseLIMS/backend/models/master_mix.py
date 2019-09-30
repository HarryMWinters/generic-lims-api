from django.db import models
import researcher


class MasterMix(models.Model):
    """
    Defines mixture used in PCR reaction (in combination with tissue sample and dna extraction).
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        researcher.Researcher, on_delete=models.PROTECT)
    primers = models.TextField(null=False)
