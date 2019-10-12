from django.db import models
from .mouse import Mouse
from .researcher import Researcher


class TissueSample(models.Model):
    """
    Defines pre DNA extraction sample.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=False, auto_created=True)
    mouse = models.ForeignKey(Mouse, null=False, on_delete=models.PROTECT)
    harvest_date = models.DateTimeField(auto_now_add=True)
    harvesting_researcher = models.ForeignKey(
        Researcher, on_delete=models.PROTECT)
