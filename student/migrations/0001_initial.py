import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0002_alter_mcq_question_primary_key'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('scholar_no', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('enrollment_no', models.CharField(max_length=20, unique=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.branch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.course')),
                ('user', models.OneToOneField(default=123, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClassRoom',
            fields=[
                ('uid', models.CharField(default=datetime.datetime.now, max_length=10, primary_key=True, serialize=False)),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.classroom')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
