from django.db import models
import protocol
import tissue_sample
import master_mix
import mouse


class PCRReaction(models.Model):
    """
    Defines defines reaction for amplifying sample post DNA extraction.
    """
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=True, auto_created=True
    )
    mouse = models.ForeignKey(
        mouse.Mouse, null=False, on_delete=models.PROTECT)
    thermocycler = models.CharField(null=False)
    pcr_protocol = models.ForeignKey(
        protocol.PCRProtocol, on_delete=models.PROTECT
    )
    # TODO Validate position string
    well_position = models.CharField(null=False)
    tissue_sample = models.ForeignKey(
        tissue_sample.TissueSample, on_delete=models.PROTECT
    )
    master_mix = models.ForeignKey(
        master_mix.MasterMix, on_delete=models.PROTECT
    )
