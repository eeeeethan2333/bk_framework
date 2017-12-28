# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0008_auto_20171222_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cpuhistory',
            options={'ordering': ['-id', '-created_time']},
        ),
        migrations.AlterField(
            model_name='cpuhistory',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 28, 18, 35, 42, 983158), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 28, 18, 35, 42, 982613)),
        ),
    ]
