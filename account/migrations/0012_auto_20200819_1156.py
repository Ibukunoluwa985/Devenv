# Generated by Django 2.2.12 on 2020-08-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileimg',
            name='profile_img',
            field=models.ImageField(default='profile_img/avatar.png', upload_to='profile_img'),
        ),
    ]
