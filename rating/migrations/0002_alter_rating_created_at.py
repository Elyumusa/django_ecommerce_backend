# Generated by Django 5.0.8 on 2024-09-02 12:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
