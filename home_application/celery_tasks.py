# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime

from celery import task
from celery.schedules import crontab
from celery.task import periodic_task
from blueking.component.shortcuts import get_client_by_request, get_client_by_user
from common.log import logger
from blueking.component.client import ComponentClient
from django.conf import settings
from models import *
import time
import re


@task()
def async_task(x, y):
    """
    定义一个 celery 异步任务
    """
    logger.error(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
    return x + y

@task()
def hello_world():
    logger.info('Hello World')


@task()
def monitor_cpu():
    try:
        client = ComponentClient(
            app_code=settings.APP_ID,
            app_secret=settings.APP_TOKEN,
            common_args={
                'username': 'admin'
            }
        )

        resp = client.job.get_task_detail({
            'app_id': '3',
            'task_id': '2'
        })

        logger.info(str(resp))
        for ip in ['10.0.1.109', '10.0.1.220', '10.0.1.188']:

            kwargs = {'app_id': '3',
                      'task_id': '2',
                      'steps': [{
                          "scriptTimeout": 1000,
                          "ipList": "1:" + ip,
                          "stepId": 2,
                          "account": "root",
                      }]}

            result = client.job.execute_task(kwargs)
            logger.info('exec task:'+str(result))
            if result.get('result', False):

                data = result['data']
                task_instance_id = data['taskInstanceId']
                complete_flag = False
                while not complete_flag:
                    time.sleep(3)
                    task_result = client.job.get_task_result({'task_instance_id': task_instance_id})
                    logger.info('fetch task result:' + str(task_result))
                    if task_result.get('result', False):
                        task_result_data = task_result['data']

                        complete_flag = task_result_data.get('isFinished', False)

                task_log = client.job.get_task_ip_log({'app_id': '3', 'task_instance_id': task_instance_id})

                task_log_analize(task_log)

    except Exception as ex:
        logger.exception(ex)


def task_log_analize(task_log):
    if not task_log or not task_log.get('result', False):
        return
    task_log_data = task_log['data'][0]

    stepAnalyseResult_list = task_log_data['stepAnalyseResult'][0]

    log_content = stepAnalyseResult_list['ipLogContent'][0]

    ip = log_content['ip']
    start_time = log_content['startTime']

    # YYYY-MM-DD HH:MM[:ss
    if start_time:
        start_time_dt = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    else:
        start_time_dt = None
    end_time = log_content['endTime']
    if end_time:
        end_time_dt = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    else:
        end_time_dt = start_time_dt

    log_content_str = log_content['logContent']

    logger.info(ip)
    logger.info(start_time)
    logger.info(log_content_str)

    usr, sys, idle = get_cpu_info(log_content_str)
    logger.info('usr='+usr)
    logger.info('sys='+sys)
    logger.info('idel='+idle)
    try:
        cpu_hist = CPUHistory.objects.create(
            ip=ip,
            created_time=start_time_dt,
            usr=float(usr),
            sys=float(sys),
            idle=float(idle)
        )
        logger.info(str(cpu_hist.id))
    except Exception as ex:
        logger.info('Exception encountered!')
        logger.exception(ex)


def get_cpu_info(log_content):
    lines = log_content.split('\n')
    logger.info(str(lines))
    if not lines or len(lines) != 7:
        return None, None, None

    data_list = re.split(r'\s+', lines[4])
    logger.info('split result:')
    logger.info(str(data_list))
    return data_list[3], data_list[5], data_list[12]


def execute_task():
    """
    执行 celery 异步任务

    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    now = datetime.datetime.now()
    logger.error(u"celery 定时任务启动，将在60s后执行，当前时间：{}".format(now))
    # 调用定时任务
    async_task.apply_async(args=[now.hour, now.minute], eta=now + datetime.timedelta(seconds=60))


@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def get_time():
    """
    celery 周期任务示例

    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    execute_task()
    now = datetime.datetime.now()
    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))
