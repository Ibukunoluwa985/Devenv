# Generated by Django 2.2.12 on 2020-08-17 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200817_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='github',
            name='branch',
        ),
        migrations.AlterField(
            model_name='github',
            name='repo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
