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
from ..base import ComponentAPI


class CollectionsBkLogin(object):
    """Collections of BK_LOGIN APIS"""

    def __init__(self, client):
        self.client = client

        self.get_all_user = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/bk_login/get_all_user/',
            description=u'获取所有用户信息',
        )
        self.get_batch_user = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/bk_login/get_batch_user/',
            description=u'获取多个用户信息',
        )
        self.get_user = ComponentAPI(
            client=self.client, method='GET', path='/api/c/compapi/bk_login/get_user/',
            description=u'获取用户信息',
        )
