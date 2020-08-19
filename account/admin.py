from django.contrib import admin
from .models import Github, Master_repo, ProfileImg

# Register your models here.

admin.site.register(Github)
admin.site.register(Master_repo)
admin.site.register(ProfileImg)