from django.db import models
from .tissue_sample import TissueSample
from .protocol import ExtractionProtocol
from .mouse import Mouse


class DNAExtraction(models.Model):
    """
    Defines 'cook' protocol.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=False, auto_created=True)
    mouse = models.ForeignKey(Mouse, null=False, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    tissue_sample = models.ForeignKey(
        TissueSample, on_delete=models.PROTECT)
    protocol = models.ForeignKey(ExtractionProtocol, on_delete=models.PROTECT)
    # TODO Validate position string
    sample_position = models.CharField(null=False, max_length=15)
