from django.db import models
import tissue_sample
import protocol
import mouse


class DNAExtraction(models.Model):
    """
    Defines 'cook' protocol.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
    mouse = models.ForeignKey(
        mouse.Mouse, null=False, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    tissue_sample = models.ForeignKey(
        tissue_sample.TissueSample, on_delete=models.PROTECT)
    protocol = models.ForeignKey(
        protocol.ExtractionProtocol, on_delete=models.PROTECT)
    # TODO Validate position string
    sample_position = models.CharField(null=False)
