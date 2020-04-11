# coding=utf-8
from __future__ import unicode_literals
from sakku import Domain, SakkuException, HttpException
from examples.config import *

try:
    app = Domain(api_key=API_KEY)

    response = app.get_domain_records(domain="mydomain.com")
    print(response)

    # OUTPUT
    # [
    #   {
    #     "comments": [],
    #     "records": [
    #       {
    #         "disabled": False,
    #         "content": "ns.sakku.cloud. hostmaster.sakku.cloud. 2019112302 5400 1800 302400 1800"
    #       }
    #     ],
    #     "reserve": True,
    #     "name": "@",
    #     "type": "SOA",
    #     "ttl": 3600
    #   },
    #   {
    #     "comments": [],
    #     "records": [
    #       {
    #         "disabled": False,
    #         "content": "ns1.sakku.cloud."
    #       },
    #       {
    #         "disabled": False,
    #         "content": "ns2.sakku.cloud."
    #       }
    #     ],
    #     "reserve": True,
    #     "name": "@",
    #     "type": "NS",
    #     "ttl": 900
    #   },
    #   {
    #     "comments": [],
    #     "records": [
    #       {
    #         "disabled": False,
    #         "content": "194.5.207.126"
    #       }
    #     ],
    #     "reserve": True,
    #     "name": "@",
    #     "type": "A",
    #     "ttl": 300
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
