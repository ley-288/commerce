# Generated by Django 3.0.6 on 2020-07-23 01:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200721_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.Listing'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 18, 20, 31, 891989)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 18, 20, 31, 891989)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 22, 18, 20, 31, 891989)),
        ),
    ]