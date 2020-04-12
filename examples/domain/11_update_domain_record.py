# coding=utf-8
from __future__ import unicode_literals

import json

from sakku import Domain, SakkuException, HttpException, RecordType
from examples.config import *

try:
    app = Domain(api_key=API_KEY)

    config = {
        "comments": [],
        "name": "B",
        "records": [
            {
                "content": "ns.sakku.cloud. hostmaster.sakku.cloud. 2019112302 5400 1800 302400 1800",
                "disabled": False
            }
        ],
        "ttl": 3600,
        "type": RecordType.SOA
    }

    response = app.update_domain_record(domain="mydomain.com", name="a", record_config=config,
                                        record_type=RecordType.SOA)

    print(response)

    # OUTPUT
    # True

    print(app.last_response().original_result())    # get raw result
    # {
    #   "code": 200,
    #   "message": "رکورد با نام a.mydomain.com. و نوع SOA تغییر کرد.",
    #   "result": True,
    #   "error": False
    # }

    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
