# Generated by Django 4.0.2 on 2022-02-12 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('user_profile', 'name')},
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('tagged_animals', models.ManyToManyField(to='main.Pet')),
            ],
        ),
    ]