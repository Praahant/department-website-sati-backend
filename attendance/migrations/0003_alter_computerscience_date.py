# Generated by Django 4.0.4 on 2022-08-01 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerscience',
            name='date',
            field=models.DateField(default=datetime.date(2022, 8, 2)),
        ),
    ]
