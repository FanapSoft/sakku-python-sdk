# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)
    config = {
        "mem": 0.2,
        "cpu": 0.2,
        "disk": 0.1
    }

    response = app.update_app_config(app_id=2688, config=config)
    print(response)
    # OUTPUT
    # {
    #   "cpu": 0.2,
    #   "mem": 0.2,
    #   "disk": 0.1,
    #   "instances": 1,
    #   "scalingMode": "OFF",
    #   "ports": [
    #     {
    #       "containerPort": 80,
    #       "hostPort": 0,
    #       "lbPort": 0,
    #       "protocol": "http",
    #       "ssl": False,
    #       "onlyInternal": False,
    #       "basicAuthentication": False,
    #       "forceRedirectHttps": False
    #     }
    #   ],
    #   "portOptions": [],
    #   "image": None,
    #   "git": None,
    #   "rebuild": False
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
