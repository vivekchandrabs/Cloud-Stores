# Generated by Django 2.1.1 on 2018-09-30 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='no_of_stores',
        ),
    ]
