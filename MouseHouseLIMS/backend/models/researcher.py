from django.contrib.auth.models import AbstractUser

from django.db import models


class Researcher(AbstractUser):
    seniority_level = models.CharField(null=False,
                                       choices=["Primary Investigator",
                                                "Senior Specialist",
                                                "Junior Specialist",
                                                "Post Doctoral Researcher",
                                                "Graduate Student",
                                                "Undergraduate",
                                                "Other"])

    def __str__(self):
        return self.email
