from django.db import models
import electrophoresis
import protocol


class GelImage(models.Model):
    """
    Defines gel image (and positive lanes etc.) from an successful electrophoresis run.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
    electrophoresis = models.ForeignKey(
        electrophoresis.Electrophoresis, on_delete=models.PROTECT)
    imaging_protocol = models.ForeignKey(
        protocol.ImagingProtocol, on_delete=models.PROTECT
    )
