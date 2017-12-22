# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0006_auto_20171222_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 59, 57, 992397), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 59, 57, 992376), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 59, 57, 991567)),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='task_instance_id',
            field=models.CharField(default=b'0', max_length=512, null=True, blank=True),
        ),
    ]
