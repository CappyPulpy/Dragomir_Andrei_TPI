from django.db import models
from django.contrib.auth.models import User

class MyUsers(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    user_data = models.IntegerField()

    class Meta:
        db_table ="myusers"
        managed = False
