# Generated by Django 3.0.7 on 2020-07-11 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20200711_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetail',
            old_name='active',
            new_name='status',
        ),
    ]