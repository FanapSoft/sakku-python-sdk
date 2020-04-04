# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, CollaboratorAccessLevel, ImageRegistryAccess
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.add_app_health_check(app_id=APP_ID, end_point="/ping", check_rate=60000, schema="https",
                                        initial_delay=1000, response_code=200, response_string="Ok.")
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 71,
    #     "endpoint": "/ping",
    #     "scheme": "https",
    #     "initialDelay": 1000,
    #     "checkRate": 60000,
    #     "responseCode": 200,
    #     "responseString": "Ok.",
    #     "lastCheck": "2020-03-17T14:00:42.915+0000",
    #     "lastResponse": "status code = 404 != 200",
    #     "lastStatus": "FAILED"
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
