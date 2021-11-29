from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.text import slugify
# from django.urls import reverse


class User(AbstractUser):
    is_data_entry_clerk = models.BooleanField(default=True)
    is_developer = models.BooleanField(default=False)
    is_ministry_of_health = models.BooleanField(default=False)
    # is_team_lead = models.BooleanField(default=False)
    # is_driver = models.BooleanField(default=False)
    pass