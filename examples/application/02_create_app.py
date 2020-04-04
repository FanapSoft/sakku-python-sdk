# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, DeployType, ScalingMode
from examples.config import *

try:
    app = Application(api_key=API_KEY)
    config = {
        "name": "PythonTest3",
        "mem": 0.1,
        "cpu": 0.1,
        "disk": 0.1,
        "ports": [
            {
                "port": 80,
                "protocol": "HTTP",
                "ssl": False,
                "onlyInternal": False,
                "basicAuthentication": False,
                "forceRedirectHttps": False
            }
        ],
        "cmd": None,
        "entrypoint": None,
        "scalingMode": ScalingMode.OFF,
        "args": [],
        "modules": [
            {
                "code": 50,
                "appId": 0,
                "metadata": {
                    "appPath": "/usr/share/nginx/html",
                    "ftp": False
                }
            }
        ],
        "environments": {},
        "labels": {},
        "netAlias": None,
        "basicAuthentications": None,
        "portOptions": None,
        "image": {
            "name": "nginx:latest",
            "registry": "dockerhub",
            "accessToken": "",
            "username": ""
        },
        "deployType": DeployType.DOCKER_IMAGE,
        "minInstance": 1,
        "maxInstance": 1,
        "network": None,
        "dependsOn": None
    }

    response = app.create_app(config=config)
    print(response)
    # OUTPUT
    # {
    #   "id": "2688",
    #   "ownerId": 197,
    #   "name": "pythontest",
    #   "uid": None,
    #   "image": "nginx:latest",
    #   "instances": None,
    #   "desc": None,
    #   "created": "2020-03-15T13:34:40.218+0000",
    #   "access": None,
    #   "configuration": {
    #     "cmd": None,
    #     "args": [],
    #     "minInstances": 1,
    #     "maxInstances": 1,
    #     "cpu": 0.1,
    #     "mem": 0.1,
    #     "disk": 0.1,
    #     "gpus": 0,
    #     "scalingMode": "OFF",
    #     "netAlias": "PythonTest"
    #   },
    #   "status": "STAGED",
    #   "deployType": "DOCKER_IMAGE",
    #   "ports": [
    #     {
    #       "type": "http",
    #       "container": 80,
    #       "lbPort": 0,
    #       "ssl": False,
    #       "onlyInternal": False,
    #       "endpoint": "wSk.default-group.e.zare.http.sakku.link",
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
