# Generated by Django 4.0.4 on 2022-07-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='classroom',
            name='section',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
