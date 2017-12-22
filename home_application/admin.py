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

# import from apps here


# import from lib
# ===============================================================================
from django.contrib import admin
from models import *
# from apps.__.models import aaaa
#
# admin.site.register(aaaa)
# ===============================================================================


@admin.register(TaskHistory)
class TaskHistoryAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id', 'created_time', 'user_name', 'task_name', 'ip', ]
    list_display_links = ['id']
    list_editable = ['created_time', 'user_name', 'task_name', 'ip', ]
    list_filter = ['user_name']
