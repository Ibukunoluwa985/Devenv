# Generated by Django 2.2.12 on 2020-08-17 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_github_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='github',
            name='branch',
            field=models.CharField(blank=True, default='https://github.com', max_length=250),
        ),
    ]
