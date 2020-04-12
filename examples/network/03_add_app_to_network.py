# coding=utf-8
from __future__ import unicode_literals
from sakku import Network, SakkuException, HttpException
from examples.config import *

try:
    app = Network(api_key=API_KEY)

    response = app.add_app_to_network(app_id=1380, name="my_network")
    print(response)
    # OUTPUT
    # True

    print(app.last_response().original_result())    # get raw result
    # {
    #   "code": 200,
    #   "message": "show-case2 با موفقیت اضافه شد!",
    #   "result": None,
    #   "error": False
    # }

    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
