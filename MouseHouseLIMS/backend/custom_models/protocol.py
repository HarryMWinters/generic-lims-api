from django.db import models
from .researcher import Researcher


class ExtractionProtocol(models.Model):
    """
    Defines a set protocol for extracting genomic DNA from a tissue sample.
    """
    author = models.ForeignKey(Researcher, on_delete=models.PROTECT)
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=False, auto_created=True
    )


class PCRProtocol(models.Model):
    """
    Defines a set PCR protocol.
    """
    author = models.ForeignKey(Researcher, on_delete=models.PROTECT)
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=False, auto_created=True
    )


class ElectrophoresisProtocol(models.Model):
    """
    Define electrophoresis protocol.
    Should include:
        voltage
        gel_composition
        time
        salts (and concentration)
        pH
        etc.
    """
    author = models.ForeignKey(Researcher, on_delete=models.PROTECT)
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=False, auto_created=True
    )


class ImagingProtocol(models.Model):
    """
    Defines how a gel was imaged (to determine DNA mobility).
    """
    author = models.ForeignKey(Researcher, on_delete=models.PROTECT)
    uuid = models.UUIDField(
        primary_key=True, unique=True, null=False, auto_created=True
    )
