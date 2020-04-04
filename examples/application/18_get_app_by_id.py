# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.get_app_by_id(app_id=APP_ID)
    print(response)
    # OUTPUT
    # {
    #   "id": "2688",
    #   "ownerId": 197,
    #   "name": "pythontest",
    #   "uid": None,
    #   "image": "nginx:latest",
    #   "instances": [
    #     {
    #       "containerId": "691f71******************************************************7081",
    #       "workerHost": "p_worker.sakku.cloud",
    #       "metadata": "sakku_worker_zone_0"
    #     }
    #   ],
    #   "desc": None,
    #   "created": "2020-03-15T13:34:40.218+0000",
    #   "access": None,
    #   "configuration": {
    #     "cmd": None,
    #     "args": [],
    #     "minInstances": 1,
    #     "maxInstances": 1,
    #     "cpu": 0.2,
    #     "mem": 0.2,
    #     "disk": 0.1,
    #     "gpus": 0.0,
    #     "scalingMode": "OFF",
    #     "netAlias": "PythonTest"
    #   },
    #   "status": "RUNNING",
    #   "deployType": "DOCKER_IMAGE",
    #   "ports": [
    #     {
    #       "type": "http",
    #       "container": 80,
    #       "lbPort": 0,
    #       "ssl": False,
    #       "onlyInternal": False,
    #       "endpoint": "wSk.default-group.e.shekari.http.sakku.link",
    #       "basicAuthentication": False,
    #       "forceRedirectHttps": False
    #     }
    #   ],
    #   "collaborative": False,
    #   "environments": {},
    #   "userModule": None,
    #   "dependency": None,
    #   "groupName": "",
    #   "basicAuthentications": []
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
