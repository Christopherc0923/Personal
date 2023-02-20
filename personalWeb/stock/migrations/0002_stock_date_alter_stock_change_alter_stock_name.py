# Generated by Django 4.1.5 on 2023-01-30 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='stock',
            name='change',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(default='U', max_length=100),
        ),
    ]
