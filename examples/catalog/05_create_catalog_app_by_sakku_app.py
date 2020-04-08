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
    #

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
