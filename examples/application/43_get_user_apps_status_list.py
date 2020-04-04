# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, Topics
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.get_user_apps_status_list()
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 2288,
    #     "status": "STAGED"
    #   },
    #   {
    #     "id": 2289,
    #     "status": "STAGED"
    #   },
    #   {
    #     "id": 2299,
    #     "status": "STAGED"
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
