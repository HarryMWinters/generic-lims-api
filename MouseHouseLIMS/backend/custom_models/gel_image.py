from django.db import models
from .electrophoresis import Electrophoresis
from .protocol import ImagingProtocol
from .mouse import Mouse


class GelImage(models.Model):
    """
    Defines gel image (and positive lanes etc.) from an successful electrophoresis run.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=False, auto_created=True)
    mouse = models.ForeignKey(
        Mouse, null=False, on_delete=models.PROTECT)
    electrophoresis = models.ForeignKey(
        Electrophoresis, on_delete=models.PROTECT)
    imaging_protocol = models.ForeignKey(
        ImagingProtocol, on_delete=models.PROTECT
    )
