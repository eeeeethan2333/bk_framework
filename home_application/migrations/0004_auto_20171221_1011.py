# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20171220_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
            ],
            options={
                'verbose_name': '\u4f5c\u5bb6',
                'verbose_name_plural': '\u4f5c\u5bb6',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u79f0')),
                ('publication_date', models.DateField(verbose_name='\u51fa\u7248\u65e5\u671f')),
                ('price', models.IntegerField(verbose_name='\u4ef7\u683c')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('authors', models.ManyToManyField(help_text='\u4f5c\u8005\u4fe1\u606f', to='home_application.Author')),
            ],
            options={
                'ordering': ['-publication_date'],
                'db_table': 'book',
                'verbose_name': '\u4e66\u7c4d',
                'verbose_name_plural': '\u4e66\u7c4d',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('address', models.CharField(max_length=64, verbose_name='\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u51fa\u7248\u793e',
                'verbose_name_plural': '\u51fa\u7248\u793e',
            },
        ),
        migrations.AlterModelOptions(
            name='taskhistory',
            options={'ordering': ['-id', '-created_time']},
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 21, 10, 11, 34, 9221)),
        ),
        migrations.AlterField(
            model_name='cpuchecktaskhistory',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 21, 10, 11, 34, 9176)),
        ),
        migrations.AlterField(
            model_name='taskhistory',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 21, 10, 11, 34, 8029)),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(help_text='\u51fa\u7248\u5546', to='home_application.Publisher'),
        ),
    ]
