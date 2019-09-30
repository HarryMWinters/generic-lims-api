from django.db import models
import mouse
import researcher


class TissueSample(models.Model):
    """
    Defines pre DNA extraction sample.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=True, auto_created=True)
    origin = models.ForeignKey(
        mouse.Mouse, null=False, on_delete=models.PROTECT)
    harvest_date = models.DateTimeField(auto_now_add=True)
    harvesting_researcher = models.ForeignKey(
        researcher.Researcher, on_delete=models.PROTECT)
