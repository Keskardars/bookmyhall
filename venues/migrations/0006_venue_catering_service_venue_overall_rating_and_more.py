# Generated by Django 4.0.2 on 2022-12-20 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0005_remove_venue_catering_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='Catering_service',
            field=models.FloatField(default='2.0'),
        ),
        migrations.AddField(
            model_name='venue',
            name='Overall_rating',
            field=models.FloatField(default='4.0'),
        ),
        migrations.AddField(
            model_name='venue',
            name='Quality_of_service',
            field=models.FloatField(default='3.0'),
        ),
        migrations.AddField(
            model_name='venue',
            name='Response_time',
            field=models.FloatField(default='3.0'),
        ),
        migrations.AddField(
            model_name='venue',
            name='Total_reviews',
            field=models.FloatField(default='4'),
        ),
    ]
