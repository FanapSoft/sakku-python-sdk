# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    # from_date = 1584200002261
    # to_date = 1584283592261
    from_date = None
    to_date = None
    save_to = None   # or file path eg. /tmp/2664.log
    response = app.logs_export(app_id=APP_ID, from_date=from_date, to_date=to_date, save_to=save_to)
    print(response)
    # OUTPUT
    #

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
