# Generated by Django 3.0.6 on 2020-07-22 04:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200721_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bid',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 21, 14, 21, 886043)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 21, 14, 21, 886043)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 21, 14, 21, 886043)),
        ),
    ]