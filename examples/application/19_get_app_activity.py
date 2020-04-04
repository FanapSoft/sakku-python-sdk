# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.get_app_activity(app_id=APP_ID)
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 359001,
    #     "created": "2020-03-17T08:18:10.370+0000",
    #     "type": "START_APP",
    #     "functor": "USER",
    #     "responder": None,
    #     "user": "e.shekari",
    #     "desc": "برنامه pythontest با موفقیت اجرا شد.",
    #     "metadata": None,
    #     "error": False,
    #     "appName": "pythontest",
    #     "appId": 2688,
    #     "request": False,
    #     "requestState": None,
    #     "allowedActions": []
    #   },
    #   {
    #     "id": 359000,
    #     "created": "2020-03-17T08:16:53.452+0000",
    #     "type": "STOP_APP",
    #     "functor": "USER",
    #     "responder": None,
    #     "user": "e.shekari",
    #     "desc": "برنامه pythontest با موفقیت متوقف شد.",
    #     "metadata": None,
    #     "error": False,
    #     "appName": "pythontest",
    #     "appId": 2688,
    #     "request": False,
    #     "requestState": None,
    #     "allowedActions": []
    #   },
    #   {
    #     "id": 358977,
    #     "created": "2020-03-15T14:13:18.044+0000",
    #     "type": "UPDATE_CONFIG",
    #     "functor": "USER",
    #     "responder": None,
    #     "user": "e.shekari",
    #     "desc": "تنظیمات برنامه pythontest با موفقیت به روز شد!",
    #     "metadata": None,
    #     "error": False,
    #     "appName": "pythontest",
    #     "appId": 2688,
    #     "request": False,
    #     "requestState": None,
    #     "allowedActions": []
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
