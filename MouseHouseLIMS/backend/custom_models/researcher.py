from django.contrib.auth.models import AbstractUser

from django.db import models


class Researcher(AbstractUser):
    seniority_level = models.CharField(null=False,
                                       max_length=63,
                                       choices=[
                                           ("Primary Investigator",
                                            "Primary Investigator"),
                                           ("Senior Specialist",
                                            "Senior Specialist"),
                                           ("Junior Specialist",
                                            "Junior Specialist"),
                                           ("Post Doctoral Researcher",
                                            "Post Doctoral Researcher"),
                                           ("Graduate Student",
                                            "Graduate Student"),
                                           ("Undergraduate",
                                            "Undergraduate"),
                                           ("Other",
                                            "Other")])
    uuid = models.UUIDField(unique=True, null=True, auto_created=True)

    def __str__(self):
        return self.email
