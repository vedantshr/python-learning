# Generated by Django 3.1 on 2020-08-12 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='location',
            new_name='location_db',
        ),
        migrations.RenameField(
            model_name='userdetails',
            old_name='username',
            new_name='username_db',
        ),
    ]