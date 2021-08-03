from django.db import models


class PollUser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=40)
