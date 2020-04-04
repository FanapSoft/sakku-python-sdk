# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, CollaboratorAccessLevel, ImageRegistryAccess
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.update_health_check_by_id(app_id=APP_ID, health_id=73, end_point="/ping", check_rate=30000,
                                             schema="https", initial_delay=2000, response_code=200,
                                             response_string="Up!!!")
    print(response)
    # OUTPUT
    # {
    #   "id": 73,
    #   "endpoint": "/ping",
    #   "scheme": "https",
    #   "initialDelay": 2000,
    #   "checkRate": 30000,
    #   "responseCode": 200,
    #   "responseString": "Up!!!",
    #   "lastCheck": "2020-03-18T05:48:27.834+0000",
    #   "lastResponse": "status code = 404 != 200",
    #   "lastStatus": "FAILED"
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
