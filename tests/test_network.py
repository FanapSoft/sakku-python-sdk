# coding=utf-8
from __future__ import unicode_literals

import unittest
import tempfile
from os import path
from random import randint
from datetime import datetime

from sakku import Network
from sakku.exceptions import *
from tests.config import *


class TestNetwork(unittest.TestCase):
    __slots__ = "__network"

    def setUp(self):
        self.__network = Network(api_key=API_KEY)

    def test_01_create_network(self):
        result = self.__network.create_network(name="unittest_network")
        self.assertIsInstance(result, dict, msg="create network : check instance")

    def test_01_create_network_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__network.create_network(name=123)

    def test_01_create_network_required_params(self):
        with self.assertRaises(TypeError):
            self.__network.create_network()

    def test_02_add_app_to_network(self):
        result = self.__network.add_app_to_network(app_id=APP_ID, name="unittest_network")
        self.assertIsInstance(result, bool, msg="add app to network : check instance")

    def test_02_add_app_to_network_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__network.add_app_to_network(app_id=str(APP_ID), name=123)

    def test_02_add_app_to_network_required_params(self):
        with self.assertRaises(TypeError):
            self.__network.add_app_to_network()

    def test_03_get_networks(self):
        result = self.__network.get_networks()
        self.assertIsInstance(result, list, msg="get networks : check instance")

    def test_04_remove_app_from_network(self):
        result = self.__network.remove_app_from_network(app_id=APP_ID, name="unittest_network")
        self.assertIsInstance(result, bool, msg="remove app from network : check instance")

    def test_04_remove_app_from_network_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__network.remove_app_from_network(app_id=str(APP_ID), name=123)

    def test_04_remove_app_from_network_required_params(self):
        with self.assertRaises(TypeError):
            self.__network.remove_app_from_network()

    def test_04_delete_network_by_user(self):
        result = self.__network.delete_network_by_user(name="unittest_network", force=True)
        self.assertIsInstance(result, bool, msg="delete network by user : check instance")

    def test_04_delete_network_by_user_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__network.delete_network_by_user(name=123, force="True")

    def test_04_delete_network_by_user_required_params(self):
        with self.assertRaises(TypeError):
            self.__network.delete_network_by_user()

