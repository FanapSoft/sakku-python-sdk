# coding=utf-8
from __future__ import unicode_literals
from sakku import Domain, SakkuException, HttpException
from examples.config import *

try:
    app = Domain(api_key=API_KEY)
    auths = [
        {
            "username": "reza",
            "password": "123456789"
        },
        {
            "username": "zare",
            "password": "123456789"
        }
    ]

    response = app.add_basic_auth_users(app_id=1380, basic_authentication=auths)
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 59,
    #     "username": "reza",
    #     "password": "123***789"
    #   },
    #   {
    #     "id": 60,
    #     "username": "zare",
    #     "password": "123***789"
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
