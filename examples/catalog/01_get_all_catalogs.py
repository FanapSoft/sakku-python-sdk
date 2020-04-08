# coding=utf-8
from __future__ import unicode_literals
from sakku import Catalog, SakkuException, HttpException
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)
    response = app.get_all_catalogs()
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 1,
    #     "name": "(CMS) سیستم مدیریت محتوا",
    #     "description": "CMSs manage the creation and modification of digital content.
    #     They typically support multiple users in a collaborative environment.",
    #     "order": 0,
    #     "created": "2019-07-20T09:09:43.036+0000",
    #     "updated": "2019-07-20T14:09:43.036+0000",
    #     "enabled": True,
    #     "vip": False,
    #     "removed": False
    #   },
    #   ...
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
