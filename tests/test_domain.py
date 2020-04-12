# coding=utf-8
from __future__ import unicode_literals

import unittest

from sakku import Domain, RecordType
from sakku.exceptions import *
from tests.config import *


class TestDomain(unittest.TestCase):
    __slots__ = "__domain"

    def setUp(self):
        self.__sample_application = None
        self.__domain = Domain(api_key=API_KEY)

    def test_01_get_all_domains_of_user(self):
        result = self.__domain.get_all_domains_of_user()
        self.assertIsInstance(result, list, msg="get all domains of user : check instance")

    def test_02_add_domain(self):
        result = self.__domain.add_domain(app_id=APP_ID, domain=DOMAIN)
        self.assertIsInstance(result, list, msg="add domain : check instance")

    def test_02_add_domain_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__domain.add_domain(app_id=str(APP_ID), domain=123)

    def test_02_add_domain_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.add_domain()

    def test_03_get_app_domains(self):
        result = self.__domain.get_app_domains(app_id=APP_ID)
        self.assertIsInstance(result, list, msg="get app domains : check instance")

    def test_03_get_app_domains_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__domain.get_app_domains(app_id=str(APP_ID))

    def test_03_get_app_domains_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.get_app_domains()

    def test_04_add_basic_auth_users(self):
        auths = [{
            "username": "reza",
            "password": "123456789"
        }]
        result = self.__domain.add_basic_auth_users(app_id=APP_ID, basic_authentication=auths)
        self.assertIsInstance(result, list, msg="add basic auth users : check instance")

    def test_04_add_basic_auth_users_validation_error(self):
        auths = [{
            "username1": "reza",
            "password2": "123456789"
        }]
        with self.assertRaises(InvalidDataException):
            self.__domain.add_basic_auth_users(app_id=str(APP_ID), basic_authentication=auths)

    def test_04_add_basic_auth_users_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.add_basic_auth_users()

    def test_05_get_basic_auth_users(self):
        result = self.__domain.get_basic_auth_users(app_id=APP_ID)
        self.assertIsInstance(result, list, msg="get basic auth users : check instance")

    def test_05_get_basic_auth_users_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__domain.get_basic_auth_users(app_id=str(APP_ID))

    def test_05_get_basic_auth_users_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.get_basic_auth_users()

    def test_06_delete_basic_auth_users(self):
        auths = self.__domain.get_basic_auth_users(app_id=APP_ID)
        if len(auths) == 0:
            self.skipTest(reason="empty basic auth users for app {}".format(APP_ID))

        result = self.__domain.delete_basic_auth_users(app_id=APP_ID, basic_auth_id=auths[0]["id"])
        self.assertIsInstance(result, list, msg="delete basic auth users : check instance")

    def test_06_delete_basic_auth_users_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__domain.delete_basic_auth_users(app_id=str(APP_ID), basic_auth_id="0")

    def test_06_delete_basic_auth_users_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.delete_basic_auth_users()

    def test_07_get_available_port_options(self):
        result = self.__domain.get_available_port_options()
        self.assertIsInstance(result, list, msg="get available port options : check instance")

    def test_08_add_domain_record(self):
        config = {
            "comments": [],
            "name": "a",
            "records": [
                {
                    "content": "ns.sakku.cloud. hostmaster.sakku.cloud. 2019112302 5400 1800 302400 1800",
                    "disabled": False
                }
            ],
            "ttl": 3600,
            "type": RecordType.SOA
        }

        result = self.__domain.add_domain_record(domain=DOMAIN, record_config=config)
        self.assertIsInstance(result, bool, msg="add domain record : check instance")

    def test_08_add_domain_record_validation_error(self):
        config = {
            "comments": [],
            # "name": "a",
            "records": [
                {
                    "content1": "ns.sakku.cloud. hostmaster.sakku.cloud. 2019112302 5400 1800 302400 1800",
                    "disabled": False
                }
            ],
            "ttl": "3600",
            # "type": RecordType.SOA
        }
        with self.assertRaises(InvalidDataException):
            self.__domain.add_domain_record(domain=123, record_config=config)

    def test_08_add_domain_record_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.add_domain_record()

    def test_09_update_domain_record(self):
        config = {
            "comments": [],
            "name": "updated_record",
            "records": [
                {
                    "content": "ns.sakku.cloud. hostmaster.sakku.cloud. 2019112302 5400 1800 302400 1800",
                    "disabled": False
                }
            ],
            "ttl": 3600,
            "type": RecordType.SOA
        }

        result = self.__domain.update_domain_record(domain=DOMAIN, name="a", record_config=config,
                                                    record_type=RecordType.SOA)
        self.assertIsInstance(result, bool, msg="update domain record : check instance")

    def test_09_update_domain_record_validation_error(self):
        config = {
            "comments": [],
            # "name": "a",
            "records": [
                {
                    "content1": "ns.sakku.cloud. hostmaster.sakku.cloud. 2019112302 5400 1800 302400 1800",
                    "disabled": False
                }
            ],
            "ttl": "3600",
            # "type": RecordType.SOA
        }
        with self.assertRaises(InvalidDataException):
            self.__domain.update_domain_record(domain=123, name="a", record_config=config, record_type=RecordType.SOA)

    def test_09_update_domain_record_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.update_domain_record()

    def test_10_get_domain_records(self):
        result = self.__domain.get_domain_records(domain=DOMAIN)
        self.assertIsInstance(result, list, msg="get domain records : check instance")

    def test_10_get_domain_records_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__domain.get_domain_records(domain=123)

    def test_10_get_domain_records_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.get_domain_records()

    def test_11_delete_domain_record(self):
        result = self.__domain.delete_domain_record(domain=DOMAIN, name="updated_record", record_type=RecordType.SOA)
        self.assertIsInstance(result, bool, msg="delete domain record : check instance")

    def test_11_delete_domain_record_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__domain.delete_domain_record(domain=123, name="123", record_type=RecordType.SOA)

    def test_11_delete_domain_record_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.delete_domain_record()

    def test_12_remove_domain(self):
        result = self.__domain.remove_domain(app_id=APP_ID, domain=DOMAIN)
        self.assertIsInstance(result, bool, msg="remove domain : check instance")
        self.assertEqual(result, True, msg="remove domain : check result")

    def test_12_remove_domain_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__domain.remove_domain(app_id=str(APP_ID), domain=123)

    def test_12_remove_domain_required_params(self):
        with self.assertRaises(TypeError):
            self.__domain.remove_domain()
