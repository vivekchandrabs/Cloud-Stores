# Generated by Django 2.1.1 on 2018-10-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0008_auto_20181020_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='phone_no',
            field=models.CharField(max_length=13),
        ),
    ]
