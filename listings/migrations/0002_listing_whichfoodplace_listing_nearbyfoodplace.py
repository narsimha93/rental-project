# Generated by Django 4.1.7 on 2023-03-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='WhichFoodPlace',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='nearByFoodPlace',
            field=models.BooleanField(default=False),
        ),
    ]
