# coding=utf-8
from __future__ import unicode_literals

from random import randint

from sakku import Catalog, SakkuException, HttpException
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)
    catalog_config = {
        "name": "کاتالوگ تست",
        "description": "این کاتالوگ با پایتون ایجاد شده.",
        "avatar": "",
        "price": 0,
        "deployLimitCount": 10,
        "catalogConfigs": [{
            "config": {
                "name": "test_catalog_{}".format(randint(10, 99)),
                "cpu": 0.1,
                "disk": 0.1,
                "mem": 0.1,
                "ports": [{
                    "port": 80,
                    "protocol": "HTTP",
                    "ssl": False,
                    "onlyInternal": False,
                    "basicAuthentication": False,
                    "forceRedirectHttps": False
                }]
            },
        }]
    }

    response = app.create_catalog_app(catalog_id=4, catalog_app_config=catalog_config)
    print(response)
    # OUTPUT
    # {
    #   "id": 90,
    #   "name": "کاتالوگ تست",
    #   "description": "این کاتالوگ با پایتون ایجاد شده.",
    #   "avatar": "",
    #   "price": 0,
    #   "deployCount": 0,
    #   "deployLimitCount": 10,
    #   "created": "2020-04-05T10:24:23.563+0000",
    #   "updated": "2020-04-05T10:24:23.564+0000",
    #   "catalogConfigs": [
    #     {
    #       "appName": None,
    #       "minCpu": 0.0,
    #       "minMem": 0.0,
    #       "minDisk": 0.0,
    #       "config": {
    #         "name": "کاتالوگ تست",
    #         "cpu": 0.1,
    #         "mem": 0.1,
    #         "disk": 0.1,
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
    #         "maxInstance": 1,
    #         "cmd": "",
    #         "entrypoint": None,
    #         "scalingMode": None,
    #         "args": None,
    #         "modules": None,
    #         "environments": {},
    #         "labels": {},
    #         "links": [],
    #         "netAliases": None,
    #         "healthChecks": [],
    #         "basicAuthentications": [],
    #         "portOptions": [],
    #         "image": None,
    #         "git": None,
    #         "app": None,
    #         "deployType": None,
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
