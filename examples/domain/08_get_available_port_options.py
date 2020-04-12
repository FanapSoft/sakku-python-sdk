# coding=utf-8
from __future__ import unicode_literals
from sakku import Domain, SakkuException, HttpException
from examples.config import *

try:
    app = Domain(api_key=API_KEY)

    response = app.get_available_port_options()
    print(response)

    # OUTPUT
    # [
    #   "client_max_body_size_in_mb",
    #   "chunked_transfer_encoding",
    #   "proxy_read_timeout_in_seconds",
    #   "limit_rate_in_kb",
    #   "client_header_buffer_size_in_kb",
    #   "client_body_timeout_in_seconds",
    #   "upstream_ip_hash"
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
