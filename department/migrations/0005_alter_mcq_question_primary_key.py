# Generated by Django 4.0.4 on 2022-07-29 23:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0004_alter_mcq_question_primary_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcq_question',
            name='primary_key',
            field=models.CharField(default=datetime.datetime(2022, 7, 30, 5, 18, 15, 905573), max_length=10, primary_key=True, serialize=False),
        ),
    ]
