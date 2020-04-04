# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.get_app_collaborators(app_id=APP_ID)
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 167,
    #     "created": "2020-03-17T11:29:45.675+0000",
    #     "expiration": "2021-03-17T11:29:44.340+0000",
    #     "accessLevel": "MODERATE",
    #     "person": {
    #       "active": True,
    #       "username": "re***re",
    #       "firstName": "رضا",
    #       "lastName": "زارع",
    #       "email": "re***re@pod.ir",
    #       "avatarUrl": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "notificationLevel": 7,
    #     "imageRegistry": ""
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
