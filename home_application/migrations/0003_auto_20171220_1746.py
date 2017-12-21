# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20171220_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='end_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 46, 15, 18081)),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='start_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 46, 15, 18056)),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 46, 15, 17475)),
        ),
    ]
