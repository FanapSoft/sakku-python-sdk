# coding=utf-8
from __future__ import unicode_literals
from sakku import Application, SakkuException, HttpException, Topics
from examples.config import *

try:
    app = Application(api_key=API_KEY)

    response = app.get_group_with_name(group_name="PythonTestDockerCompose")
    print(response)

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
