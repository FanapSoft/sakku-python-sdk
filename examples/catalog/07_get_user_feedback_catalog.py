# coding=utf-8
from __future__ import unicode_literals

from random import randint

from sakku import Catalog, SakkuException, HttpException
from examples.config import *

try:
    app = Catalog(api_key=API_KEY)

    response = app.get_user_feedback_catalog()
    print(response)
    # OUTPUT
    # []

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
