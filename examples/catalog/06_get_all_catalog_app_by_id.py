# coding=utf-8
from __future__ import unicode_literals

from random import randint

from sakku import Catalog, SakkuException, HttpException
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)

    response = app.get_all_catalog_app_by_id(catalog_id=4)
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 27,
    #     "name": "MongoDB",
    #     "description": "description",
    #     "avatar": "https://podspace.pod.ir/nzh/drive/downloadFile?hash=2U9TO421NZWT77Z2",
    #     "price": 0,
    #     "deployCount": 4,
    #     "deployLimitCount": 1000,
    #     "created": "2019-08-10T13:39:36.848+0000",
    #     "updated": "2020-01-07T09:38:20.315+0000",
    #     "catalogConfigs": [
    #       {
    #         "appName": None,
    #         "minCpu": 0.2,
    #         "minMem": 1.0,
    #         "minDisk": 1.0,
    #         "config": {
    #           "name": "mongoDB",
    #           "cpu": 1.0,
    #           "mem": 1.0,
    #           "disk": 1.0,
    #           "ports": [
    #             {
    #               "host": 0,
    #               "port": 27017,
    #               "protocol": "tcp",
    #               "ssl": False,
    #               "onlyInternal": False,
    #               "basicAuthentication": False,
    #               "forceRedirectHttps": False
    #             },
    #             {
    #               "host": 0,
    #               "port": 27018,
    #               "protocol": "tcp",
    #               "ssl": False,
    #               "onlyInternal": False,
    #               "basicAuthentication": False,
    #               "forceRedirectHttps": False
    #             },
    #             {
    #               "host": 0,
    #               "port": 27019,
    #               "protocol": "tcp",
    #               "ssl": False,
    #               "onlyInternal": False,
    #               "basicAuthentication": False,
    #               "forceRedirectHttps": False
    #             }
    #           ],
    #           "minInstance": 1,
    #           "maxInstance": 1,
    #           "cmd": "",
    #           "entrypoint": None,
    #           "scalingMode": "OFF",
    #           "args": [],
    #           "modules": [
    #             {
    #               "code": 50,
    #               "appId": 0,
    #               "metadata": {
    #                 "appPath": "/data/db"
    #               }
    #             },
    #             {
    #               "code": 10,
    #               "appId": 0,
    #               "metadata": {
    #                 "envDbNameKeyName": "MONGODB_DATABASE",
    #                 "envUsernameKeyName": "MONGODB_USER",
    #                 "envPasswordKeyName": "MONGODB_PASS",
    #                 "reusable": "True"
    #               }
    #             }
    #           ],
    #           "environments": {},
    #           "labels": {},
    #           "links": [],
    #           "netAliases": None,
    #           "healthChecks": [],
    #           "basicAuthentications": [],
    #           "portOptions": [],
    #           "image": {
    #             "name": "mongo:3.4.22",
    #             "registry": "dockerhub",
    #             "accessToken": "",
    #             "username": ""
    #           },
    #           "git": None,
    #           "app": None,
    #           "deployType": "DOCKER_IMAGE",
    #           "worker": None,
    #           "network": None,
    #           "dependsOn": None,
    #           "pipeLineStatus": "WAITING"
    #         },
    #         "dockerFileText": None,
    #         "metadata": []
    #       }
    #     ]
    #   },
    #   ...
    #  ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
