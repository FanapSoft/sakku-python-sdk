# coding=utf-8
from __future__ import unicode_literals
from sakku import Domain, SakkuException, HttpException
from examples.config import *

try:
    app = Domain(api_key=API_KEY)

    response = app.get_app_domains(app_id=1380)
    print(response)
    # OUTPUT
    # [
    #   {
    #     "domain": "mydomain.com",
    #     "nameServer": [
    #       {
    #         "current": "NS1.MYDOMAIN.COM",
    #         "error": True
    #       },
    #       {
    #         "current": "NS2.MYDOMAIN.COM",
    #         "error": True
    #       },
    #       {
    #         "current": "NS3.MYDOMAIN.COM",
    #         "error": True
    #       },
    #       {
    #         "current": "NS4.MYDOMAIN.COM",
    #         "error": True
    #       }
    #     ],
    #     "cert": None,
    #     "state": "OK"
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
