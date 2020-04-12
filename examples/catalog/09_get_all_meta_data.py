# coding=utf-8
from __future__ import unicode_literals

from random import randint

from sakku import Catalog, SakkuException, HttpException
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)

    response = app.get_all_meta_data()
    print(response)
    # OUTPUT
    # [
    #   {
    #     "name": "version",
    #     "scope": "CONFIG",
    #     "description": "use this to add versionality to your catalog app, value will be set in image tag"
    #   },
    #   {
    #     "name": "short_open_tag",
    #     "scope": "ENV",
    #     "description": "use this to add [name] environment to your catalog app, value will be set in environments:
    #     [name]=[value]"
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
