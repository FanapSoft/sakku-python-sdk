# coding=utf-8
from __future__ import unicode_literals

from random import randint

from sakku import Catalog, SakkuException, HttpException
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)
    catalog_config = {
        "name": "کاتالوگ تست - ویرایش شده",
        "description": "این کاتالوگ با پایتون ایجاد شده.",
        "avatar": "",
        "price": 0,
        "deployLimitCount": 100,
        "catalogConfigs": [{
            "config": {
                "name": "test_c_edi_{}".format(randint(10, 99)),
                "cpu": 0.2,
                "disk": 0.2,
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
            "metadata": [
                {
                    "advanced": False,
                    "scope": "APP"
                }
            ]
        }]
    }

    response = app.update_catalog(catalog_app_id=90, catalog_app_config=catalog_config)
    print(response)
    # OUTPUT
    #

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
