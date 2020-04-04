# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, Topics
from examples.config import *

try:
    app = Application(api_key=API_KEY)
    config = {
        "name": "MachineMechanismPython",
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
        "scalingMode": "OFF",
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
        "deployType": "DOCKER_IMAGE",
        "minInstance": 1,
        "maxInstance": 1,
        "network": None,
        "dependsOn": None
    }
    response = app.create_app_by_machine_mechanism(config=config)
    print(response)

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
