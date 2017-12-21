# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0004_auto_20171221_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 21, 15, 9, 9, 931544), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 21, 15, 9, 9, 931518), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 21, 15, 9, 9, 930750)),
        ),
    ]
