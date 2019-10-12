from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .custom_models.researcher import Researcher

# Register your models here.

admin.site.register(Researcher, UserAdmin)
