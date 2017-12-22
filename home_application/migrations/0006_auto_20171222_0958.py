# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0005_auto_20171221_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskhistory',
            name='task_instance_id',
            field=models.CharField(max_length=512, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 58, 59, 368456), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 58, 59, 368433), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 9, 58, 59, 367600)),
        ),
    ]
