# Generated by Django 3.2.3 on 2021-06-07 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_auto_20210607_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recreation',
            old_name='no_people',
            new_name='no_days',
        ),
    ]
