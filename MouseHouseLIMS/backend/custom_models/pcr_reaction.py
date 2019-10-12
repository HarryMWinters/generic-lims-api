from django.db import models
from .protocol import PCRProtocol
from .tissue_sample import TissueSample
from .master_mix import MasterMix
from .mouse import Mouse


class PCRReaction(models.Model):
    """
    Defines defines reaction for amplifying sample post DNA extraction.
    """
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=False, auto_created=True
    )
    mouse = models.ForeignKey(
        Mouse, null=False, on_delete=models.PROTECT)
    thermocycler = models.CharField(null=False, max_length=63)
    pcr_protocol = models.ForeignKey(
        PCRProtocol, on_delete=models.PROTECT
    )
    # TODO Validate position string
    well_position = models.CharField(null=False, max_length=15)
    tissue_sample = models.ForeignKey(
        TissueSample, on_delete=models.PROTECT
    )
    master_mix = models.ForeignKey(
        MasterMix, on_delete=models.PROTECT
    )
