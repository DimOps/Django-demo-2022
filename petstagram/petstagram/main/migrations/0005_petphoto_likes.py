# Generated by Django 4.0.2 on 2022-02-13 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_pet_user_profile_alter_pet_unique_together_petphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]