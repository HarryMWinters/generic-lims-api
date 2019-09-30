from django.db import models


class Mouse(models.Model):
    """
    Define murine model for genotyping.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=False, auto_created=True)
    date_of_birth = models.DateField(null=False)
    sex = models.CharField(null=False, max_length=1,
                           choices=["F", "M"], min_length=1)
    cage_number = models.IntegerField(null=False)
    ear_mark = models.CharField(null=False, choices=[
                                "right-notch", "left-notch", "right-vee", "left-vee", "double-vee", "double-notch"])
    genotype = models.CharField(null=True, choices=["FOO+", "FOO-", "WT"])
