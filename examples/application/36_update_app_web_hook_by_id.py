# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, Topics
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    config = {
        "secured": True,
        "topics": Topics.ALL,
        "url": "https://karthing.ir/test.php?platform=sakku&webhook=15"
    }

    response = app.update_app_web_hook_by_id(app_id=APP_ID, web_hook_id=15, config=config)
    print(response)
    # OUTPUT
    # {
    #   "id": 15,
    #   "url": "https://karthing.ir/test.php?platform=sakku&webhook=15",
    #   "topics": "ALL",
    #   "token": "********-****-****-****-************",
    #   "secured": True
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
