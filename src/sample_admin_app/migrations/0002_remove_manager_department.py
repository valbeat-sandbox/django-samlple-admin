# Generated by Django 2.2.10 on 2020-03-04 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample_admin_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='department',
        ),
    ]