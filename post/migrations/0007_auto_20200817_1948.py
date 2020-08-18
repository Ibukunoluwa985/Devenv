# Generated by Django 2.2.12 on 2020-08-17 19:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20200817_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code_body',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
