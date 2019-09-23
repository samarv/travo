from django.db import models

# Create your models here.


class organizations(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50, unique=True)
    slack_org_id = models.CharField(max_length=50, unique=True)
    channel_name = models.CharField(max_length=50, required=False)
    channel_id = models.CharField(max_length=50, required=False)
    access_token = models.CharField(max_length=200)
    installation_date = models.DateTimeField('installation date', null=True)
    bot_access_token = models.CharField(max_length=200)
