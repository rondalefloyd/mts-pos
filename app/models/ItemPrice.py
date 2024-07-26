# myapp/models.py

from django.db import models
from datetime import datetime

class User(models.Model):
    organization_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    access_code = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=255, null=True, blank=True)
    access_level = models.IntegerField(null=True, blank=True)
    active_status = models.IntegerField(null=True, blank=True)
    last_login_ts = models.CharField(max_length=255, null=True, blank=True)
    last_logout_ts = models.CharField(max_length=255, null=True, blank=True)
    update_ts = models.CharField(max_length=255, default=datetime.now, blank=True)

    def __str__(self):
        return self.username
