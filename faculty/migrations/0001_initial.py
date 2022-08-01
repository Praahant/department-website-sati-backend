# Generated by Django 4.0.4 on 2022-07-30 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('faculty_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('adhar_no', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('faculty_name', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_joining', models.DateField(default=django.utils.timezone.now)),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('email2', models.EmailField(blank=True, max_length=254, null=True)),
                ('faculty_image', models.ImageField(blank=True, default='', null=True, upload_to='faculty/images')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('title_of_event', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('enclosure_no', models.IntegerField(unique=True)),
                ('attended', models.CharField(default='[]', max_length=10000)),
                ('organised', models.CharField(default='[]', max_length=10000)),
                ('category', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('duration', models.DateTimeField()),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OutreachActivity',
            fields=[
                ('enclosure_no', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('organisation', models.CharField(max_length=100)),
                ('nameOfActivity', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FacultyOutreachActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.contactdetails')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.outreachactivity')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.event')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculty.contactdetails')),
            ],
        ),
    ]
