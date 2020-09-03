# Generated by Django 3.0.6 on 2020-07-20 04:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Lucas Sousa', max_length=32),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=32)),
                ('desc_short', models.CharField(max_length=64)),
                ('desc_long', models.CharField(max_length=1024)),
                ('price_start', models.DecimalField(decimal_places=2, max_digits=8)),
                ('url', models.CharField(max_length=128)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 7, 19, 21, 40, 50, 175307))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 7, 19, 21, 40, 50, 176307))),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_bid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 7, 19, 21, 40, 50, 175307))),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(to='auctions.Listing'),
        ),
    ]