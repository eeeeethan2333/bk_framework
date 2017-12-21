# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='end_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 46, 8, 715080)),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='log_info',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='start_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 46, 8, 715057)),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 46, 8, 714392)),
        ),
        migrations.AlterModelTable(
            name='cpuchecktaskhistory',
            table='cpu_task_hist',
        ),
        migrations.AlterModelTable(
            name='taskhistory',
            table='task_hist',
        ),
    ]
