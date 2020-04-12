# coding=utf-8
from __future__ import unicode_literals
from sakku import Network, SakkuException, HttpException
from examples.config import *

try:
    app = Network(api_key=API_KEY)

    response = app.create_network(name="my_network")
    print(response)
    # OUTPUT
    # {
    #   "id": 223,
    #   "created": "2020-04-11T10:45:28.189+0000",
    #   "updated": "2020-04-11T10:45:28.189+0000",
    #   "name": "my_network",
    #   "owner": {
    #     "id": 173,
    #     "username": "r*****e",
    #     "mobile": "0937*****41",
    #     "active": True,
    #     "firstName": "رضا",
    #     "lastName": "زارع",
    #     "email": "r*****e@pod.ir",
    #     "avatarUrl": "https://core.pod.ir:443/nzh/image/?imageId=...",
    #     "nationalNumber": None,
    #     "isRemoved": False
    #   },
    #   "apps": [],
    #   "subnet": "10.0.116.0/24",
    #   "gateway": "10.0.116.1",
    #   "default": False
    # }

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
