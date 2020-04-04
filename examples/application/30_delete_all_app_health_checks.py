# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, CollaboratorAccessLevel, ImageRegistryAccess
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.delete_all_app_health_checks(app_id=APP_ID, path="/ping")
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 71,
    #     "endpoint": "/ping",
    #     "scheme": "https",
    #     "initialDelay": 0,
    #     "checkRate": 0,
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
