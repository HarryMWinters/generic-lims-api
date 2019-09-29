from django.db import models


class PCR_Reaction(models.Model):
    """
    Defines defines reaction for amplifying sample post DNA extraction.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
