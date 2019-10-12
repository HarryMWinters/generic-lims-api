from django.db import models
from .pcr_reaction import PCRReaction
from .protocol import ElectrophoresisProtocol
from .mouse import Mouse


class Electrophoresis(models.Model):
    """
    Defines gel electrophoresis protocol run on amplified sample.
    """
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=False, auto_created=True
    )
    lane_position = models.IntegerField(null=False)
    electrophoresis_protocol = models.ForeignKey(
        ElectrophoresisProtocol, on_delete=models.PROTECT
    )
    mouse = models.ForeignKey(
        Mouse, null=False, on_delete=models.PROTECT)
