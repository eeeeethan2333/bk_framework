# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_request, get_client_by_user
from django.http import JsonResponse
from models import TaskHistory, CPUCheckTaskHistory
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import logging
# Get an instance of a logger
logger = logging.getLogger('root')

def home(request):
    app_id = request.GET.get('app_id', '3')
    # task = request.GET.get('')
    client = get_client_by_request(request)
    server_list = []
    resp = client.cc.get_app_host_list({'app_id': app_id})
    if resp.get('result', False):
        server_list.extend(resp.get('data'))
        logger.info(server_list)
    return render_mako_context(request, '/home_application/home.html', {'server_list': server_list})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def test(request):
    app_id = request.GET.get('app_id', '0')
    client = get_client_by_request(request)

    result = client.cc.get_app_host_list({'app_id': app_id})
    logger.info(client.bk_login.get_user())

    return render_json(result)


def celery_test():
    user = 'public'
    client = get_client_by_user(user)
    kwargs = {'app_id': 1}
    result = client.cc.get_app_host_list(kwargs)


@csrf_exempt
def check_cpu(request):
    return_data = {'result': False}
    ip = request.POST.get('ip', None)
    try:
        client = get_client_by_request(request)
        kwargs = {'app_id': '3',
                  'task_id': '2',
                  'steps': [{
                        "scriptTimeout": 1000,
                        "ipList": "1:"+ip,
                        "stepId": 2,
                        "account": "root",
                }]}

        result = client.job.execute_task(kwargs)
        if result.get('result', False):
            return_data['result'] = True
            data = result['data']
            task_hist = TaskHistory.objects.create(user_name=request.user.username, task_name=data['taskInstanceName'], ip=ip)

            kwargs = {'app_id': '3', 'task_instance_id': data['taskInstanceId']}
            task_log = client.job.get_task_ip_log(kwargs)

            if task_log.get('result', False):
                task_log_data = task_log['data'][0]

                stepAnalyseResult_list = task_log_data['stepAnalyseResult'][0]

                log_content = stepAnalyseResult_list['ipLogContent'][0]

                ip = log_content['ip']
                start_time = log_content['startTime']
                end_time = log_content['endTime']
                log_content_str = log_content['logContent']
                CPUCheckTaskHistory.objects.create(
                    task_hist=task_hist,
                    result_status='S',
                    ip=ip,
                    start_time=start_time,
                    end_time=end_time if end_time else start_time,
                    log_info=log_content_str
                )
            else:
                CPUCheckTaskHistory.objects.create(
                    task_hist=task_hist,
                    result_status='F',
                    ip=ip,

                )
    except Exception as ex:
        logger.exception(ex)
        return_data = {'result': False}

    # result = client.cc.get_app_host_list(kwargs)
    # return result
    return JsonResponse(return_data)


def task_history(request):

    try:
        task_hist_list = [task_hist.to_json() for task_hist in TaskHistory.objects.all()]

    except Exception as ex:
        logger.exception(ex)
        task_hist_list = []
    return JsonResponse({'task_hist_list': task_hist_list})


def history_detail(request, task_hist_id=None):
    data = {
        'result': False
    }

    try:
        if not task_hist_id:
            raise ValidationError('Invalid task_hist_id')


    except Exception as ex:
        logger.exception(ex)
        data['result'] = False
        data['hist_detail'] = None

    return JsonResponse(data)

