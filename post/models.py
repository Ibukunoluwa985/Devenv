from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

# Create your models here.

# post creation model
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,)
    title = models.CharField(max_length=500, blank=True, null=True,)
    body = models.CharField(max_length=5000, blank=True, null=True,)
    code_body = RichTextField(max_length=20000, blank=True, null=True,)
    language = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

# post creation form
class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post

        exclude = ('user',)

        fields = (
            'title',
            'language',
            'body',
            'code_body',
        )

        labels = {
            'title': _(''),
            'language': _(''),
            'body': _(''),
            'code_body': _(''),
        }

        widgets = {
            'title': forms.TextInput(attrs=
            {
                'class': 'form-control validate text-center text-black',
                'placeholder': 'Question title',
            }),
            'language': forms.TextInput(attrs=
            {
                'class': 'form-control validate text-center text-black',
                'placeholder': 'Question language eg: Python',
            }),
            'body': forms.Textarea(attrs=
            {
                'class': 'form-control validate text-center text-black',
                'placeholder': 'Your Question Here',
                'required': 'required',
                'cols': '40',
                'rows': '5',
            }),
            'code_body': forms.Textarea(attrs=
            {
                'class': 'form-control validate text-center text-black',
                'placeholder': 'Code',
            }),
        }