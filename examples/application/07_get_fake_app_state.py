# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException
from examples.config import *

try:
    app = Application(api_key=API_KEY)
    response = app.get_fake_app_state(app_id=APP_ID)
    print(response)
    # OUTPUT
    # {
    #   "code": 11,
    #   "title": "پایان بارگذاری",
    #   "message": null,
    #   "percent": 100,
    #   "deployQueueId": "96246b1b-a3d2-4664-beac-384f6dd91690",
    #   "steps": [
    #     {
    #       "code": 1,
    #       "title": "بارگذاری هنوز آغاز نشده است!",
    #       "passed": true
    #     },
    #     {
    #       "code": 3,
    #       "title": "آغاز ساخت ماژول ها",
    #       "passed": true
    #     },
    #     {
    #       "code": 4,
    #       "title": "در حال ساخت ماژول Storage",
    #       "passed": true
    #     },
    #     {
    #       "code": 5,
    #       "title": "در حال ساخت ماژول DBaas",
    #       "passed": true
    #     },
    #     {
    #       "code": 7,
    #       "title": "در حال بارگذاری ایمیج روی سرور",
    #       "passed": true
    #     },
    #     {
    #       "code": 8,
    #       "title": "در حال تنظیم دامنه های برنامه",
    #       "passed": true
    #     },
    #     {
    #       "code": 9,
    #       "title": "در حال اعمال تنظیمات نهایی",
    #       "passed": true
    #     },
    #     {
    #       "code": 10,
    #       "title": "در حال بررسی سلامت برنامه",
    #       "passed": true
    #     },
    #     {
    #       "code": 11,
    #       "title": "پایان بارگذاری",
    #       "passed": true
    #     }
    #   ],
    #   "updated": "2020-03-11T06:09:31.476+0000"
    # }
    # {
    #   "code": 11,
    #   "title": "پایان بارگذاری",
    #   "message": None,
    #   "percent": 100.0,
    #   "deployQueueId": "c2fb5d79-c9e8-4706-b1b8-4a51ad028d22",
    #   "steps": [
    #     {
    #       "code": 1,
    #       "title": "بارگذاری هنوز آغاز نشده است!",
    #       "passed": True
    #     },
    #     {
    #       "code": 3,
    #       "title": "آغاز ساخت ماژول ها",
    #       "passed": True
    #     },
    #     {
    #       "code": 4,
    #       "title": "در حال ساخت ماژول Storage",
    #       "passed": True
    #     },
    #     {
    #       "code": 7,
    #       "title": "در حال بارگذاری ایمیج روی سرور",
    #       "passed": True
    #     },
    #     {
    #       "code": 8,
    #       "title": "در حال تنظیم دامنه های برنامه",
    #       "passed": True
    #     },
    #     {
    #       "code": 9,
    #       "title": "در حال اعمال تنظیمات نهایی",
    #       "passed": True
    #     },
    #     {
    #       "code": 10,
    #       "title": "در حال بررسی سلامت برنامه",
    #       "passed": True
    #     },
    #     {
    #       "code": 11,
    #       "title": "پایان بارگذاری",
    #       "passed": True
    #     }
    #   ],
    #   "updated": "2020-03-15T13:34:40.218+0000"
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
