from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Github(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.CharField(max_length=250, blank=True, null=True)

class Master_repo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    repo = models.CharField(max_length=250, blank=True, null=True)