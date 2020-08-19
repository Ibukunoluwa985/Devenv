from django.db import models
from django import forms

# Create your models here.

from django.contrib.auth.models import User

class Github(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.CharField(max_length=250, blank=True, null=True)

class Master_repo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    repo = models.CharField(max_length=250, blank=True, null=True)

class ProfileImg(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_img', default='profile_img/avatar.png')

class ProfileImgForm(forms.ModelForm):
    
    class Meta:

        model = ProfileImg

        fields = ('profile_img',)