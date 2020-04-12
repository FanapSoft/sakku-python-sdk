# coding=utf-8
from __future__ import unicode_literals

import unittest
from datetime import datetime
from random import randint

from sakku import Catalog, FeedbackType, MetaDataScope
from sakku.exceptions import *
from tests.config import *


class TestCatalog(unittest.TestCase):
    __slots__ = "__catalog"

    def setUp(self):
        self.__sample_application = None
        self.__catalog = Catalog(api_key=API_KEY)

    def test_01_get_all_catalogs(self):
        result = self.__catalog.get_all_catalogs()
        self.assertIsInstance(result, list, msg="get all catalogs : check instance")

    def test_02_create_catalog_app(self):
        catalog_id = randint(100, 999)
        catalog_config = {
            "name": "کاتالوگ تست {}".format(catalog_id),
            "description": "این کاتالوگ با پایتون ایجاد شده.",
            "avatar": "",
            "price": 0,
            "deployLimitCount": 10,
            "catalogConfigs": [{
                "config": {
                    "name": "catalog_{}".format(catalog_id),
                    "cpu": 0.1,
                    "disk": 0.1,
                    "mem": 0.1,
                    "ports": [{
                        "port": 80,
                        "protocol": "HTTP",
                        "ssl": False,
                        "onlyInternal": False,
                        "basicAuthentication": False,
                        "forceRedirectHttps": False
                    }]
                },
            }]
        }

        result = self.__catalog.create_catalog_app(catalog_id=4, catalog_app_config=catalog_config)
        self.assertIsInstance(result, dict, msg="create catalog app : check instance")
        self.assertEqual(result["name"], catalog_config["name"], msg="create catalog app : check name")

    def test_02_create_catalog_app_validation_error(self):
        catalog_id = randint(100, 999)
        catalog_config = {
            "name": "کاتالوگ تست {}".format(catalog_id),
            "description": "این کاتالوگ با پایتون ایجاد شده.",
            "avatar": "",
            "price": "0",
            "deployLimitCount": "10",
            "catalogConfigs": [{
                "config": {
                    "name": "catalog_{}".format(catalog_id),
                    "cpu": 0.1,
                    "disk": 0.1,
                    "mem": 0.1,
                    "ports": [{
                        "port": 80,
                        "protocol": "HTTP",
                        "ssl": False,
                        "onlyInternal": False,
                        "basicAuthentication": False,
                        "forceRedirectHttps": False
                    }]
                },
            }]
        }

        with self.assertRaises(InvalidDataException):
            self.__catalog.create_catalog_app(catalog_id="4", catalog_app_config=catalog_config)

    def test_02_create_catalog_app_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.create_catalog_app()

    def test_03_update_catalog(self):
        catalog_id = randint(100, 999)
        catalog_config = {
            "name": "کاتالوگ تست {}".format(catalog_id),
            "description": "این کاتالوگ با پایتون ویرایش شده.",
            "avatar": "",
            "price": 0,
            "deployLimitCount": 10,
            "catalogConfigs": [{
                "config": {
                    "name": "catalog_{}".format(catalog_id),
                    "cpu": 0.1,
                    "disk": 0.1,
                    "mem": 0.1,
                    "ports": [{
                        "port": 80,
                        "protocol": "HTTP",
                        "ssl": False,
                        "onlyInternal": False,
                        "basicAuthentication": False,
                        "forceRedirectHttps": False
                    }]
                },
            }]
        }

        result = self.__catalog.update_catalog(catalog_app_id=90, catalog_app_config=catalog_config)
        self.assertIsInstance(result, dict, msg="update catalog app : check instance")
        self.assertEqual(result["name"], catalog_config["name"], msg="update catalog app : check name")

    def test_03_update_catalog_validation_error(self):
        catalog_id = randint(100, 999)
        catalog_config = {
            "name": "کاتالوگ تست {}".format(catalog_id),
            "description": "این کاتالوگ با پایتون ویرایش شده.",
            "avatar": "",
            "price": "0",
            "deployLimitCount": "10",
            "catalogConfigs": [{
                "config": {
                    "name": "catalog_{}".format(catalog_id),
                    "cpu": 0.1,
                    "disk": 0.1,
                    "mem": 0.1,
                    "ports": [{
                        "port": 80,
                        "protocol": "HTTP",
                        "ssl": False,
                        "onlyInternal": False,
                        "basicAuthentication": False,
                        "forceRedirectHttps": False
                    }]
                },
            }]
        }

        with self.assertRaises(InvalidDataException):
            self.__catalog.update_catalog(catalog_app_id="90", catalog_app_config=catalog_config)

    def test_03_update_catalog_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.update_catalog()

    def test_04_get_catalog_app(self):
        result = self.__catalog.get_catalog_app(catalog_id=4, catalog_app_id=90)
        self.assertIsInstance(result, list, msg="get catalog app : check instance")

    def test_04_get_catalog_app_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__catalog.get_catalog_app(catalog_id="4", catalog_app_id="90")

    def test_04_get_catalog_app_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.get_catalog_app()

    def test_05_create_catalog_app_by_sakku_app(self):
        catalog_config = {
            "name": "کاتالوگ تستی",
            "description": "این کاتالوگ با پایتون و از روی یک برنامه ایجاد شده است.",
            "avatar": "",
            "price": 0,
            "deployLimitCount": 10,
            "catalogConfigs": [{
                "appName": "CatalogAppTest",
                "minCpu": 0.1,
                "minDisk": 0.1,
                "minMem": 0.1,
            }]
        }
        result = self.__catalog.create_catalog_app_by_sakku_app(catalog_id=4, app_id=1380,
                                                                catalog_app_config=catalog_config)
        self.assertIsInstance(result, dict, msg="create catalog app by sakku app : check instance")

    def test_05_create_catalog_app_by_sakku_app_validation_error(self):
        catalog_config = {
            # "name": "کاتالوگ تستی",
            # "description": "این کاتالوگ با پایتون و از روی یک برنامه ایجاد شده است.",
            # "avatar": "",
            "price": "0",
            "deployLimitCount": "10",
            "catalogConfigs": [{
                "appName": "CatalogAppTest",
                "minCpu": 0.1,
                "minDisk": 0.1,
                "minMem": 0.1,
            }]
        }

        with self.assertRaises(InvalidDataException):
            self.__catalog.create_catalog_app_by_sakku_app(catalog_id="4", app_id="1380",
                                                           catalog_app_config=catalog_config)

    def test_05_create_catalog_app_by_sakku_app_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.create_catalog_app_by_sakku_app()

    def test_06_get_all_catalog_app_by_id(self):
        result = self.__catalog.get_all_catalog_app_by_id(catalog_id=4)
        self.assertIsInstance(result, list, msg="get all catalog app by id : check instance")

    def test_06_get_all_catalog_app_by_id_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__catalog.get_all_catalog_app_by_id(catalog_id="4")

    def test_06_get_all_catalog_app_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.get_all_catalog_app_by_id()

    def test_07_get_user_feedback_catalog(self):
        result = self.__catalog.get_user_feedback_catalog(status=False)
        self.assertIsInstance(result, list, msg="get user feedback catalog : check instance")

    def test_07_get_user_feedback_catalog_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__catalog.get_user_feedback_catalog(status="False")

    def test_08_add_user_feedback_catalogs(self):
        result = self.__catalog.add_user_feedback_catalogs(subject="بازخورد تستی",
                                                           description="این یک بازخورد تستی است",
                                                           feedback_type=FeedbackType.IMPROVEMENT)
        self.assertIsInstance(result, bool, msg="add user feedback catalog : check instance")

    def test_08_add_user_feedback_catalogs_all_params(self):
        result = self.__catalog.add_user_feedback_catalogs(subject="بازخورد تستی",
                                                           description="این یک بازخورد تستی است",
                                                           feedback_type=FeedbackType.IMPROVEMENT,
                                                           catalogApp=90, dockerName="test", price=1000,
                                                           minCpu=0.1, minMem=0.1, minDisk=0.1)
        self.assertIsInstance(result, bool, msg="add user feedback catalog : check instance")

    def test_08_add_user_feedback_catalogs_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__catalog.add_user_feedback_catalogs(subject="بازخورد تستی",
                                                      description="این یک بازخورد تستی است",
                                                      feedback_type=FeedbackType.IMPROVEMENT,
                                                      catalogApp="90", dockerName="test", price="1000",
                                                      minCpu="0.1", minMem="0.1", minDisk="0.1")

    def test_08_add_user_feedback_catalogs_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.add_user_feedback_catalogs()

    def test_09_get_all_meta_data(self):
        result = self.__catalog.get_all_meta_data()
        self.assertIsInstance(result, list, msg="get all metadata : check instance")

    def test_09_get_all_meta_data_all_params(self):
        result = self.__catalog.get_all_meta_data(page=1, size=10)
        self.assertIsInstance(result, list, msg="get all metadata (all params) : check instance")

    def test_09_get_all_meta_data_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__catalog.get_all_meta_data(page="1", size="10")

    def test_10_validate_meta_data(self):
        result = self.__catalog.validate_meta_data(meta_data={
            "name": "version",
            "scope": MetaDataScope.CONFIG
        })
        self.assertIsInstance(result, dict, msg="validate metadata : check instance")

    def test_10_validate_meta_data_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__catalog.validate_meta_data(meta_data="{\"name\":\"version\",\"scope\":\"CONFIG\"}")

    def test_10_validate_meta_data_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.validate_meta_data()

    def test_11_deploy_app_from_catalog_test(self):
        settings = {
            "name": "newapp",
            "mem": 0.1,
            "cpu": 0.2,
            "disk": 0.1,
            "metadata": [
                {
                    "name": "version",
                    "scope": "CONFIG",
                    "value": "latest"
                }
            ]
        }
        result = self.__catalog.deploy_app_from_catalog_test(catalog_app_id=4, settings=settings)
        self.assertIsInstance(result, dict, msg="validate metadata : check instance")

    def test_11_deploy_app_from_catalog_test_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__catalog.deploy_app_from_catalog_test(catalog_app_id="4", settings="", files="")

    def test_11_deploy_app_from_catalog_test_required_params(self):
        with self.assertRaises(TypeError):
            self.__catalog.deploy_app_from_catalog_test()
