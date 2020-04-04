# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    params = {
        "commit": True,     # commit application status. the oldest container.
        "tag": ""   # version of application. empty = now in format:yyyy-MM-dd-HH-mm-ss
    }

    response = app.stop_app_by_id(app_id=APP_ID, **params)
    print(response)
    # OUTPUT
    # برنامه با شناسه 2688 با موفقیت متوقف شد!

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
