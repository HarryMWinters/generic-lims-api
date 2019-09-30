from django.db import models
import pcr_reaction
import protocol


class Electrophoresis(models.Model):
    """
    Defines gel electrophoresis protocol run on amplified sample.
    """
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=True, auto_created=True
    )
    lane_position = models.IntegerField(null=False)
    electrophoresis_protocol = models.ForeignKey(
        protocol.ElectrophoresisProtocol, on_delete=models.PROTECT
    )