# Generated by Django 3.1 on 2020-08-19 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno_db', models.TextField(default='NA')),
                ('price_db', models.TextField(default='NA')),
                ('year_db', models.TextField(default='NA')),
                ('company_db', models.TextField(default='NA')),
                ('RAM_db', models.TextField(default='NA')),
                ('ROM_db', models.TextField(default='NA')),
            ],
        ),
    ]
