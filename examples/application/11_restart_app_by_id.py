# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    params = {
        "commitStart": False,   # load from committed image
        "commitStop": False,    # commit application status. the oldest container. Default : False
        "tagStart": "latest",   # load from committed image with tag. Default : latest
        "tagStop": "",  # version of application in format:yyyy-MM-dd-HH-mm-ss. empty = now
    }

    response = app.restart_app_by_id(app_id=APP_ID, **params)
    print(response)
    # OUTPUT
    # True

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
