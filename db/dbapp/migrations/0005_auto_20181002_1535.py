# Generated by Django 2.1.1 on 2018-10-02 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0004_userdetail_no_of_stores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storeid', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('itemname', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrderShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_shop', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('shopkeeper_name', models.CharField(blank=True, max_length=100)),
                ('phone_no', models.IntegerField(blank=True, default=0)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.Store')),
            ],
        ),
        migrations.AddField(
            model_name='order_item',
            name='order_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.OrderShop'),
        ),
    ]
