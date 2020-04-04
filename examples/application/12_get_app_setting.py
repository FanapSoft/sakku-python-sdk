# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.get_app_setting(app_id=APP_ID)
    print(response)
    # OUTPUT
    # {
    #   "id": 2688,
    #   "name": "pythontest",
    #   "cpu": 0.2,
    #   "mem": 0.2,
    #   "disk": 0.1,
    #   "image": {
    #     "name": "nginx",
    #     "registry": "dockerhub",
    #     "username": None,
    #     "tag": "latest",
    #     "createDate": 1584279280182,
    #     "buildSuccessfully": True,
    #     "autoBuildUUID": None
    #   },
    #   "git": None,
    #   "minInstance": 1,
    #   "maxInstance": 1,
    #   "cmd": None,
    #   "entrypoint": None,
    #   "scalingMode": "OFF",
    #   "args": [],
    #   "modules": [
    #     {
    #       "code": 50,
    #       "appId": 0,
    #       "metadata": {
    #         "ftp": "false",
    #         "appPath": "/usr/share/nginx/html"
    #       }
    #     }
    #   ],
    #   "environments": {},
    #   "deployType": "DOCKER_IMAGE",
    #   "lastRestartReason": None,
    #   "lastTaskFailure": None,
    #   "currentInstances": 1,
    #   "lastScalingAt": 1584281585443,
    #   "instances": [
    #     {
    #       "containerId": "1b9**********************************************************9ec",
    #       "workerHost": "worker2.sakku.cloud",
    #       "internalIP": "10.0.63.28",
    #       "metadata": "",
    #       "uptimeSeconds": 147480,
    #       "stagedAt": 1584281591200,
    #       "startedAt": 1584281593600
    #     }
    #   ],
    #   "deploymentIds": [],
    #   "network": "default_user_network_197",
    #   "jsonConfig": {
    #     "name": "PythonTest",
    #     "cpu": 0.2,
    #     "mem": 0.2,
    #     "disk": 0.1,
    #     "ports": [
    #       {
    #         "host": 0,
    #         "port": 80,
    #         "protocol": "http",
    #         "ssl": False,
    #         "onlyInternal": False,
    #         "basicAuthentication": False,
    #         "forceRedirectHttps": False
    #       }
    #     ],
    #     "minInstance": 1,
    #     "maxInstance": 1,
    #     "cmd": "",
    #     "entrypoint": None,
    #     "scalingMode": "OFF",
    #     "args": [],
    #     "modules": [
    #       {
    #         "code": 50,
    #         "appId": 0,
    #         "metadata": {
    #           "ftp": "false",
    #           "appPath": "/usr/share/nginx/html"
    #         }
    #       }
    #     ],
    #     "environments": {},
    #     "labels": {},
    #     "links": [],
    #     "netAlias": None,
    #     "healthChecks": [],
    #     "basicAuthentications": [],
    #     "portOptions": [],
    #     "image": {
    #       "name": "nginx:latest",
    #       "registry": "dockerhub",
    #       "accessToken": "",
    #       "username": ""
    #     },
    #     "git": None,
    #     "app": None,
    #     "deployType": "DOCKER_IMAGE",
    #     "worker": None,
    #     "network": None,
    #     "dependsOn": None,
    #     "pipeLineStatus": "RUNNING"
    #   }
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
