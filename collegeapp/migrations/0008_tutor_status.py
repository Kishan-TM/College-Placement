# Generated by Django 5.1.3 on 2024-11-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0007_tutor_pswd'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]