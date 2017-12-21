# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPUCheckTaskHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result_status', models.CharField(default=b'F', max_length=3, choices=[(b'F', b'Failed'), (b'S', b'Succeed')])),
                ('ip', models.CharField(max_length=512)),
                ('start_time', models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 10, 6, 15198))),
                ('end_time', models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 10, 6, 15220))),
                ('log_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created_time', models.DateTimeField(verbose_name=datetime.datetime(2017, 12, 20, 17, 10, 6, 14605))),
                ('user_name', models.CharField(max_length=512)),
                ('task_name', models.CharField(max_length=512)),
                ('ip', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='cpuchecktaskhistory',
            name='task_hist',
            field=models.OneToOneField(to='home_application.TaskHistory'),
        ),
    ]
