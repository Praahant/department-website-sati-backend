# Generated by Django 4.0.4 on 2022-07-29 22:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0003_alter_mcq_question_primary_key'),
        ('faculty', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerScience',
            fields=[
                ('primary_key', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PRESENT', 'Present'), ('ABSENT', 'Absent'), ('LEAVE', 'Leave')], max_length=50, verbose_name='status')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateField(default=datetime.date(2022, 7, 30))),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.contactdetails')),
            ],
        ),
    ]
