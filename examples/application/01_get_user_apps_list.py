# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)
    response = app.get_user_apps_list(page=1, size=10)
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": "2664",
    #     "ownerId": 197,
    #     "name": "newapp",
    #     "uid": None,
    #     "image": None,
    #     "instances": None,
    #     "desc": None,
    #     "created": "2020-03-11T06:09:31.475+0000",
    #     "access": None,
    #     "configuration": None,
    #     "status": "RUNNING",
    #     "deployType": "DOCKER_IMAGE",
    #     "ports": None,
    #     "collaborative": False,
    #     "environments": None,
    #     "userModule": None,
    #     "dependency": None,
    #     "groupName": "",
    #     "basicAuthentications": None
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
