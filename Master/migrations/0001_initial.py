# Generated by Django 3.0.2 on 2020-06-27 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('depname', models.CharField(choices=[('CE', 'Civil Engineering'), ('CSE', 'Computer Science Engineering'), ('EEE', 'Electrical Engineering'), ('ECE', 'Electronics and Communications Engineering'), ('ISE', 'Information Science Engineering'), ('ME', 'Mechanical Engineering'), ('BS', 'Basic Science')], max_length=3, primary_key=True, serialize=False)),
                ('dep_email', models.CharField(default='', max_length=50)),
                ('dep_contact', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usn', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=40)),
                ('sem', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth')], default=1)),
                ('phone', models.CharField(default='', max_length=12)),
                ('parent_phone', models.CharField(default='', max_length=12)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=40)),
                ('ph_no', models.CharField(max_length=10)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.Department')),
                ('faculty', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('course_name', models.CharField(default='', max_length=50)),
                ('total_classes', models.IntegerField(default=0)),
                ('sem', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth')], default=1)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.Department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_attendance', models.IntegerField(default=0)),
                ('percent', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.Course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Master.Faculty')),
                ('usn', models.ForeignKey(db_column='usn', on_delete=django.db.models.deletion.CASCADE, to='Master.Student')),
            ],
        ),
    ]
