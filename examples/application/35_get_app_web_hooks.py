# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, CollaboratorAccessLevel, ImageRegistryAccess
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.get_app_web_hooks(app_id=APP_ID)
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 15,
    #     "url": "https://karthing.ir/test.php?platform=sakku",
    #     "topics": "ALL",
    #     "token": "********-****-****-****-************",
    #     "secured": True
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
