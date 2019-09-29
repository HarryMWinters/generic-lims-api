from django.db import models


class Electrophoresis(models.Model):
    """
    Defines gel electrophoresis protocol run on amplified sample.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
