from django.db import models
from django import forms

# Create your models here.

# post creation model
class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=5000)
    language = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)


# post creation form
class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'language',
        )

        widgets = {
            'title': forms.TextInput(attrs=
            {
                'class': 'form-control text-center text-black',
                'placeholder': 'Question title',
            }),
            'body': forms.Textarea(attrs=
            {
                'class': 'form-control text-center text-black',
                'cols': '50',
                'rows': '25',
                'placeholder': 'Question',
            }),
            'language': forms.TextInput(attrs=
            {
                'class': 'form-control text-center text-black',
                'placeholder': 'Question language',
            }),
        }