from django.db import models

class SalesGroup(models.Model):
    sales_group_id = models.AutoField(primary_key=True)
    sales_group_name = models.CharField(max_length=255, null=True, blank=True)
    update_ts = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sales_group_name
