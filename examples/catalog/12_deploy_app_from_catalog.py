# coding=utf-8
from __future__ import unicode_literals

from random import randint

from sakku import Catalog, SakkuException, HttpException, MetaDataScope
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)

    settings = {
        "name": "newapp",
        "mem": 1,
        "cpu": 0.2,
        "disk": 2,
        "metadata": [
            {
                "name": "version",
                "scope": "CONFIG",
                "value": "latest"
            }
        ]
    }

    response = app.deploy_app_from_catalog(catalog_app_id=21, settings=settings)
    print(response)
    # OUTPUT
    #

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
