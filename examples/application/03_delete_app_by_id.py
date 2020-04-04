# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, DeployType, ScalingMode
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.delete_app_by_id(app_id=2714, force=True)
    print(response)
    # OUTPUT
    # برنامه با شناسه 2714 با موفقیت حذف شد!

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
