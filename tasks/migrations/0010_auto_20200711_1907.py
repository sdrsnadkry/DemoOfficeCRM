# Generated by Django 3.0.7 on 2020-07-11 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20200711_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='status',
            new_name='active',
        ),
    ]
