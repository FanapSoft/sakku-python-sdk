# coding=utf-8
from __future__ import unicode_literals
from sakku import Network, SakkuException, HttpException
from examples.config import *

try:
    app = Network(api_key=API_KEY)

    response = app.get_networks()
    print(response)
    # OUTPUT
    # [
    #   {
    #     "id": 45,
    #     "created": "2019-12-21T14:02:15.557+0000",
    #     "updated": "2020-01-20T07:30:38.682+0000",
    #     "name": "default_user_network_173",
    #     "owner": {
    #       "id": 173,
    #       "username": "r*****e",
    #       "mobile": "0937*****41",
    #       "active": True,
    #       "firstName": "رضا",
    #       "lastName": "زارع",
    #       "email": "r****re@pod.ir",
    #       "avatarUrl": "https://core.pod.ir:443/nzh/image/?imageId=...",
    #       "nationalNumber": None,
    #       "isRemoved": False
    #     },
    #     "apps": [
    #       2805
    #     ],
    #     "subnet": "10.0.42.0/24",
    #     "gateway": "10.0.42.1",
    #     "default": True
    #   }
    # ]

    # print(app.last_response().original_result())    # get raw result
    # print(app.last_response())  # get response handler

except HttpException as e:
    print("Http Exception\nMessage : {}\nStatus Code : {}\n".format(e.message, e.status_code))
    # print(e.response_handler)
except SakkuException as e:
    print("Sakku Exception\nMessage : {}".format(e.message))
