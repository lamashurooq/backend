# Generated by Django 2.1.7 on 2019-03-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190318_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseinstructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructorname', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructorname',
        ),
        migrations.AddField(
            model_name='courseinstructure',
            name='courseName',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]
