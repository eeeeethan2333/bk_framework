# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0007_auto_20171222_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPUHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ip', models.CharField(max_length=512)),
                ('created_time', models.DateTimeField(default=datetime.datetime(2017, 12, 22, 11, 52, 20, 589106), null=True, blank=True)),
                ('usr', models.FloatField(null=True, blank=True)),
                ('sys', models.FloatField(null=True, blank=True)),
                ('idle', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cpu_hist',
            },
        ),
        migrations.RemoveField(
            model_name='cpuchecktaskhistory',
            name='task_hist',
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 22, 11, 52, 20, 588516)),
        ),
        migrations.DeleteModel(
            name='CPUCheckTaskHistory',
        ),
    ]
