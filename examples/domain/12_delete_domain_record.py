# coding=utf-8
from __future__ import unicode_literals

import json

from sakku import Domain, SakkuException, HttpException, RecordType
from examples.config import *

try:
    app = Domain(api_key=API_KEY)

    response = app.delete_domain_record(domain="mydomain.com", name="a", record_type=RecordType.SOA)

    print(response)

    # OUTPUT
    # True

    print(app.last_response().original_result())    # get raw result
    # {
    #   "code": 200,
    #   "message": "رکورد با نام a.mydomain.com. و نوع SOA مربوط به دامنه mydomain.com حذف شد.",
    #   "result": True,
    #   "error": False
    # }

    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
