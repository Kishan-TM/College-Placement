# Generated by Django 5.1.3 on 2024-12-17 07:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0021_delete_jobapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeapp.joblisting')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeapp.student')),
            ],
        ),
    ]