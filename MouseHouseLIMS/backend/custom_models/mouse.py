from django.db import models


class Mouse(models.Model):
    """
    Define murine model for genotyping.
    """
    uuid = models.UUIDField(primary_key=True, unique=True,
                            null=False, auto_created=True)
    date_of_birth = models.DateField(null=False)
    sex = models.CharField(null=False, max_length=1,
                           choices=[
                               ("F", "F"),
                               ("M", "M")])
    cage_number = models.IntegerField(null=False)
    ear_mark = models.CharField(null=False, max_length=20,
                                choices=[
                                    ("right-notch", "right-notch"),
                                    ("left-notch", "left-notch"),
                                    ("right-vee", "right-vee"),
                                    ("left-vee", "left-vee"),
                                    ("double-vee", "double-vee"),
                                    ("double-notch", "double-notch")])
    genotype = models.CharField(null=True, max_length=5,
                                choices=[
                                    ("FOO+", "FOO+"),
                                    ("FOO-", "FOO-"),
                                    ("WT", "WT")])
