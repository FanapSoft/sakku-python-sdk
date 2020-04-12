# coding=utf-8
from __future__ import unicode_literals

from random import randint

from sakku import Catalog, SakkuException, HttpException
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)

    catalog_config = {
        "name": "کاتالوگ تستی",
        "description": "این کاتالوگ با پایتون و از روی یک برنامه ایجاد شده است.",
        "avatar": "",
        "price": 0,
        "deployLimitCount": 10,
        "catalogConfigs": [{
            "appName": "CatalogAppTest",
            "minCpu": 0.1,
            "minDisk": 0.1,
            "minMem": 0.1,
        }]
    }

    response = app.create_catalog_app_by_sakku_app(app_id=1380, catalog_id=4, catalog_app_config=catalog_config)
    print(response)
    # OUTPUT
    # {
    #   "id": 94,
    #   "name": "کاتالوگ تستی",
    #   "description": "این کاتالوگ با پایتون و از روی یک برنامه ایجاد شده است.",
    #   "avatar": "",
    #   "price": 0,
    #   "deployCount": 0,
    #   "deployLimitCount": 10,
    #   "created": "2020-04-12T05:01:08.912+0000",
    #   "updated": "2020-04-12T05:01:08.912+0000",
    #   "catalogConfigs": [
    #     {
    #       "appName": "CatalogAppTest",
    #       "minCpu": 0.1,
    #       "minMem": 0.1,
    #       "minDisk": 0.1,
    #       "config": {
    #         "name": "کاتالوگ تستی",
    #         "cpu": 0.1,
    #         "mem": 0.1,
    #         "disk": 1.0,
    #         "ports": [
    #           {
    #             "host": 0,
    #             "port": 80,
    #             "protocol": "http",
    #             "ssl": False,
    #             "onlyInternal": False,
    #             "basicAuthentication": False,
    #             "forceRedirectHttps": False
    #           }
    #         ],
    #         "minInstance": 1,
    #         "maxInstance": 2,
    #         "cmd": "",
    #         "entrypoint": None,
    #         "scalingMode": "OFF",
    #         "args": [],
    #         "modules": [],
    #         "environments": {},
    #         "labels": {},
    #         "links": [],
    #         "netAliases": None,
    #         "healthChecks": [],
    #         "basicAuthentications": [
    #           {
    #             "username": "reza",
    #             "password": "123456789"
    #           },
    #           {
    #             "username": "zare",
    #             "password": "123456789"
    #           }
    #         ],
    #         "portOptions": [],
    #         "image": {
    #           "name": "http://reg.sakku.cloud/r*****e/podshowcase:v1",
    #           "registry": "dockerhub",
    #           "accessToken": "",
    #           "username": ""
    #         },
    #         "git": None,
    #         "app": None,
    #         "deployType": "DOCKER_IMAGE",
    #         "worker": None,
    #         "network": "",
    #         "dependsOn": None,
    #         "pipeLineStatus": "WAITING"
    #       },
    #       "dockerFileText": None,
    #       "metadata": []
    #     }
    #   ]
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
