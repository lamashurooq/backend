# Generated by Django 2.1.7 on 2019-03-18 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrule',
            old_name='user',
            new_name='userid',
        ),
    ]
