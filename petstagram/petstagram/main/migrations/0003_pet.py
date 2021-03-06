# Generated by Django 4.0.2 on 2022-02-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile_date_of_birth_profile_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bunny', 'Bunny'), ('Parrot', 'Parrot'), ('Fish', 'Fish'), ('Other', 'Other')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
