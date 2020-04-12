# coding=utf-8
from __future__ import unicode_literals
from sakku import Domain, SakkuException, HttpException
from examples.config import *

try:
    app = Domain(api_key=API_KEY)

    response = app.remove_domain(app_id=1380, domain="mydomain.com")
    print(response)
    # OUTPUT
    # True

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
