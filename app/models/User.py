from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    organization_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    access_code = models.CharField(max_length=255, unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)
    access_level = models.IntegerField(null=True, blank=True)
    active_status = models.BooleanField(default=True)
    last_login_ts = models.DateTimeField(null=True, blank=True)
    last_logout_ts = models.DateTimeField(null=True, blank=True)
    update_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
