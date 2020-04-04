# coding=utf-8
from __future__ import unicode_literals

import unittest
import tempfile
from os import path
from random import randint
from datetime import datetime

from sakku import Application, DeployType, ScalingMode, Topics, ImageRegistryAccess, CollaboratorAccessLevel
from sakku.exceptions import *
from tests.config import *


def sample_app_config(name=None):
    if name is None:
        name = "app{}".format(datetime.now().__format__("%Y%m%d_%H%M%S"))

    return {
        "name": name,
        "mem": 0.1,
        "cpu": 0.1,
        "disk": 0.1,
        "ports": [
            {
                "port": 80,
                "protocol": "HTTP",
                "ssl": False,
                "onlyInternal": False,
                "basicAuthentication": False,
                "forceRedirectHttps": False
            }
        ],
        "cmd": None,
        "entrypoint": None,
        "scalingMode": ScalingMode.OFF,
        "args": [],
        "modules": [
            {
                "code": 50,
                "appId": 0,
                "metadata": {
                    "appPath": "/usr/share/nginx/html",
                    "ftp": False
                }
            }
        ],
        "environments": {},
        "labels": {},
        "netAlias": None,
        "basicAuthentications": None,
        "portOptions": None,
        "image": {
            "name": "nginx:latest",
            "registry": "dockerhub",
            "accessToken": "",
            "username": ""
        },
        "deployType": DeployType.DOCKER_IMAGE,
        "minInstance": 1,
        "maxInstance": 1,
        "network": None,
        "dependsOn": None
    }


def sample_web_hook_config(app_id):
    return {
        "secured": True,
        "topics": Topics.ALL,
        "url": "https://karthing.ir/test.php?platform=sakku&app_id={}".format(app_id)
    }


class TestApplication(unittest.TestCase):
    __slots__ = "__app"

    def setUp(self):
        self.__sample_application = None
        self.__app = Application(api_key=API_KEY)
        self.__docker_compose_name = ""
        try:
            self.__app_for_transfer = self.__app.create_app(config=sample_app_config())
        except Exception as e:
            self.__app_for_transfer = None

    def test_01_get_user_apps_list(self):
        result = self.__app.get_user_apps_list()

        self.assertIsInstance(result, list, "get user apps list : check instance")

    def test_01_get_user_apps_list_all_params(self):
        result = self.__app.get_user_apps_list(page=1, size=10)

        self.assertIsInstance(result, list, "get user apps list (all params) : check instance")

    def test_01_get_user_apps_list_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.get_user_apps_list(page="1", size="10")

    def test_02_create_app(self):
        config = sample_app_config()
        result = self.__app.create_app(config=config)

        self.assertIsInstance(result, dict, "create app : check instance")
        app_config = result["configuration"]
        self.assertEqual(app_config["cpu"], config["cpu"], "create app : check cpu")
        self.assertEqual(app_config["mem"], config["mem"], "create app : check mem")

    def test_02_create_app_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.create_app()

    def test_02_create_app_validation_error(self):
        config = {
            "cpu": "0.1"
        }
        with self.assertRaises(InvalidDataException):
            self.__app.create_app(config=config)

    def __sample_app(self):
        self.__sample_application = {
            "id": 2688
        }

        if self.__sample_application is None:
            self.__sample_application = self.__app.create_app(config=sample_app_config())
        return self.__sample_application

    def test_04_commit_app_container(self):
        app = self.__sample_app()
        result = self.__app.commit_app_container(app_id=int(app["id"]))

        self.assertIsInstance(result, str, "commit app container : check instance")

    def test_04_commit_app_container_all_params(self):
        app = self.__sample_app()
        random = randint(10000000, 99999999)
        container_id = "container_id_{}".format(random)
        tag = "tag_{}".format(random)
        result = self.__app.commit_app_container(app_id=int(app["id"]), container_id=container_id, tag=tag)

        self.assertIsInstance(result, str, "commit app container (all params) : check instance")

    def test_04_commit_app_container_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.commit_app_container()

    def test_04_commit_app_container_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.commit_app_container(app_id=app_id)

    def test_05_update_app_config(self):
        app = self.__sample_app()
        config = sample_app_config()
        config["cpu"] = 0.2
        result = self.__app.update_app_config(app_id=int(app["id"]), config=config)

        self.assertIsInstance(result, dict, "update app config : check instance")

    def test_05_update_app_config_all_params(self):
        app = self.__sample_app()
        random = randint(10000000, 99999999)
        container_id = "container_id_{}".format(random)
        tag = "tag_{}".format(random)
        result = self.__app.update_app_config(app_id=int(app["id"]), container_id=container_id, tag=tag)

        self.assertIsInstance(result, dict, "update app config (all params) : check instance")

    def test_05_update_app_config_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.update_app_config()

    def test_05_update_app_config_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.update_app_config(app_id=app_id)

    def test_06_get_real_time_deploy(self):
        app = self.__sample_app()
        result = self.__app.get_real_time_deploy(app_id=int(app["id"]))

        self.assertIsInstance(result, dict, "get real time deploy : check instance")

    def test_06_get_real_time_deploy_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_real_time_deploy()

    def test_06_get_real_time_deploy_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_real_time_deploy(app_id=app_id)

    def test_07_get_fake_app_state(self):
        app = self.__sample_app()
        result = self.__app.get_fake_app_state(app_id=int(app["id"]))

        self.assertIsInstance(result, dict, "get fake app state : check instance")

    def test_07_get_fake_app_state_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_fake_app_state()

    def test_07_get_fake_app_state_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_fake_app_state(app_id=app_id)

    def test_08_logs_export(self):
        app = self.__sample_app()
        result = self.__app.logs_export(app_id=int(app["id"]))

        self.assertIsInstance(result, str, "logs export : check instance")

    def test_08_logs_export_save_to_file(self):
        app = self.__sample_app()
        path_file_log = "{}/python_{}.log".format(tempfile.gettempdir(), app["id"])
        self.__app.logs_export(app_id=int(app["id"]), save_to=path_file_log)

        self.assertTrue(path.isfile(path_file_log), "logs export (save to file): check file exists")

    def test_08_logs_export_all_params(self):
        app = self.__sample_app()
        result = self.__app.logs_export(app_id=int(app["id"]), from_date=1584200002261, to_date=1584283592261)

        self.assertIsInstance(result, str, "logs export (all params): check instance")

    def test_08_logs_export_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.logs_export()

    def test_08_logs_export_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.logs_export(app_id=app_id, from_date="123456789", to_date="12345678900")

    def test_09_get_app_owner(self):
        app = self.__sample_app()
        result = self.__app.get_app_owner(app_id=int(app["id"]))

        self.assertIsInstance(result, dict, "get app owner : check instance")

    def test_09_get_app_owner_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_owner()

    def test_09_get_app_owner_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_owner(app_id=app_id)

    def test_10_rebuild_app(self):
        app = self.__sample_app()
        try:
            result = self.__app.rebuild_app(app_id=int(app["id"]))
            self.assertIsInstance(result, dict, "rebuild app : check instance")
        except HttpException as e:
            self.assertEqual(e.status_code, 400, "rebuild app : check status_code 400")

    def test_10_rebuild_app_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.rebuild_app()

    def test_10_rebuild_app_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.rebuild_app(app_id=app_id)

    def test_11_restart_app_by_id(self):
        app = self.__sample_app()
        result = self.__app.restart_app_by_id(app_id=int(app["id"]))
        self.assertIsInstance(result, bool, "restart app by id : check instance")

    def test_11_restart_app_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.restart_app_by_id()

    def test_11_restart_app_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.restart_app_by_id(app_id=app_id)

    def test_12_get_app_setting(self):
        app = self.__sample_app()
        result = self.__app.get_app_setting(app_id=int(app["id"]))
        self.assertIsInstance(result, dict, "get app setting : check instance")

    def test_12_get_app_setting_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_setting()

    def test_12_get_app_setting_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_setting(app_id=app_id)

    def test_13_start_app_by_id(self):
        app = self.__sample_app()
        try:
            result = self.__app.start_app_by_id(app_id=int(app["id"]))
            self.assertIsInstance(result, str, "start app by id : check instance")
        except HttpException as e:
            self.assertEqual(e.status_code, 400, "start app by id : check status_code 400")

    def test_13_start_app_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.start_app_by_id()

    def test_13_start_app_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.start_app_by_id(app_id=app_id)

    def test_14_stop_app_by_id(self):
        app = self.__sample_app()
        try:
            result = self.__app.stop_app_by_id(app_id=int(app["id"]))
            self.assertIsInstance(result, str, "stop app by id : check instance")
            self.__start_app_for_next_test(int(app["id"]))
        except HttpException as e:
            self.assertEqual(e.status_code, 400, "stop app by id : check status_code 400")

    def __start_app_for_next_test(self, app_id):
        try:
            self.__app.start_app_by_id(app_id)
        except Exception:
            pass

    def test_14_stop_app_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.stop_app_by_id()

    def test_14_stop_app_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.stop_app_by_id(app_id=app_id)

    def test_15_stop_app_deploy(self):
        app = self.__sample_app()
        try:
            result = self.__app.stop_app_deploy(app_id=int(app["id"]))
            self.assertIsInstance(result, str, "stop app deploy : check instance")
        except HttpException as e:
            self.assertEqual(e.status_code, 400, "stop app deploy : check status_code 400")

    def test_15_stop_app_deploy_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.stop_app_deploy()

    def test_15_stop_app_deploy_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.stop_app_deploy(app_id=app_id)

    def test_16_get_app_versions(self):
        app = self.__sample_app()

        result = self.__app.get_app_versions(app_id=int(app["id"]))
        self.assertIsInstance(result, list, "get app versions : check instance")

    def test_16_get_app_versions_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_versions()

    def test_16_get_app_versions_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_versions(app_id=app_id)

    def test_17_create_app_web_hooks(self):
        app = self.__sample_app()
        config = sample_web_hook_config(app["id"])

        result = self.__app.create_app_web_hooks(app_id=int(app["id"]), config=config)
        self.assertIsInstance(result, dict, "create app web hooks : check instance")
        self.assertEqual(result["topics"], config["topics"], "create app web hooks : check topics")

    def test_17_create_app_web_hooks_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.create_app_web_hooks()

    def test_17_create_app_web_hooks_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.create_app_web_hooks(app_id=app_id, config={})

    def test_18_get_app_by_id(self):
        app = self.__sample_app()

        result = self.__app.get_app_by_id(app_id=int(app["id"]))
        self.assertIsInstance(result, dict, "get app by id : check instance")

    def test_18_get_app_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_by_id()

    def test_18_get_app_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_by_id(app_id=app_id)

    def test_19_get_app_activity(self):
        app = self.__sample_app()

        result = self.__app.get_app_activity(app_id=int(app["id"]))
        self.assertIsInstance(result, list, "get app activity : check instance")

    def test_19_get_app_activity_all_params(self):
        app = self.__sample_app()

        result = self.__app.get_app_activity(app_id=int(app["id"]), page=1, size=10)
        self.assertIsInstance(result, list, "get app activity (all params) : check instance")

    def test_19_get_app_activity_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_activity()

    def test_19_get_app_activity_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_activity(app_id=app_id)

    def test_20_get_chat_data(self):
        app = self.__sample_app()

        try:
            result = self.__app.get_chat_data(app_id=int(app["id"]))
            self.assertIsInstance(result, list, "get chat data : check instance")
        except HttpException as e:
            self.assertEqual(e.status_code, 400, "get chat data : check status code 400")

    def test_20_get_chat_data_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_chat_data()

    def test_20_get_chat_data_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_chat_data(app_id=app_id)

    def test_21_check_app_health(self):
        app = self.__sample_app()

        result = self.__app.check_app_health(app_id=int(app["id"]))
        self.assertIsInstance(result, list, "check app health : check instance")

    def test_21_check_app_health_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.check_app_health()

    def test_21_check_app_health_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.check_app_health(app_id=app_id)

    def test_22_check_app_health_by_id(self):
        app = self.__sample_app()

        health_list = self.__app.get_app_health_check(app_id=int(app["id"]))
        if len(health_list) == 0:
            self.skipTest("check app health by id : empty health check")

        result = self.__app.check_app_health_by_id(app_id=int(app["id"]), health_id=health_list[0]["id"])
        self.assertIsInstance(result, dict, "check app health by id : check instance")

    def test_22_check_app_health_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.check_app_health_by_id()

    def test_22_check_app_health_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.check_app_health_by_id(app_id=app_id, health_id="123")

    def test_23_get_app_collaborators(self):
        app = self.__sample_app()

        result = self.__app.get_app_collaborators(app_id=int(app["id"]))
        self.assertIsInstance(result, list, "get app collaborators : check instance")

    def test_23_get_app_collaborators_all_params(self):
        app = self.__sample_app()

        result = self.__app.get_app_collaborators(app_id=int(app["id"]), page=1, size=50, all_collaborators=True)
        self.assertIsInstance(result, list, "get app collaborators (all params) : check instance")

    def test_23_get_app_collaborators_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_collaborators()

    def test_23_get_app_collaborators_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_collaborators(app_id=app_id, page="1", size="10", all_collaborators="True")

    def test_24_add_app_collaborator(self):
        app = self.__sample_app()
        try:
            result = self.__app.add_app_collaborator(app_id=int(app["id"]), email=COLLABORATOR_EMAIL,
                                                     access_level=CollaboratorAccessLevel.MODERATE,
                                                     image_registry_access=ImageRegistryAccess.ALL,
                                                     level=7)
            self.assertIsInstance(result, dict, "add app collaborator : check instance")
        except HttpException as e:
            self.assertEqual(e.status_code, 409, "add app collaborator : check status code 409")

    def test_24_add_app_collaborator_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.add_app_collaborator()

    def test_24_add_app_collaborator_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.add_app_collaborator(app_id=app_id, page="1", size="10", all_collaborators="True")

    def test_25_update_app_collaborator(self):
        app = self.__sample_app()
        collaborators = self.__app.get_app_collaborators(app_id=int(app["id"]))
        if len(collaborators) == 0:
            self.skipTest("update app collaborator : collaborator not found")

        result = self.__app.update_app_collaborator(app_id=int(app["id"]), collaborator_id=collaborators[0]["id"],
                                                    email=COLLABORATOR_EMAIL,
                                                    access_level=CollaboratorAccessLevel.MODERATE,
                                                    image_registry_access=ImageRegistryAccess.PULL,
                                                    level=6)
        self.assertIsInstance(result, dict, "update app collaborator : check instance")

    def test_25_update_app_collaborator_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.update_app_collaborator()

    def test_25_update_app_collaborator_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.update_app_collaborator(app_id=app_id, collaborator_id="123", email="asda", access_level="ABCD",
                                               image_registry_access="ABCD", level="5")

    def test_26_delete_app_collaborator(self):
        app = self.__sample_app()
        collaborators = self.__app.get_app_collaborators(app_id=int(app["id"]))
        if len(collaborators) == 0:
            self.skipTest("delete app collaborator : collaborator not found")

        result = self.__app.delete_app_collaborator(app_id=int(app["id"]), collaborator_id=collaborators[0]["id"])
        self.assertIsInstance(result, str, "delete app collaborator : check instance")

    def test_26_delete_app_collaborator_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.delete_app_collaborator()

    def test_26_delete_app_collaborator_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.delete_app_collaborator(app_id=app_id, collaborator_id="45674")

    def test_27_verify_user_command_permission(self):
        app = self.__sample_app()

        result = self.__app.verify_user_command_permission(app_id=int(app["id"]), cmd="rm -rf")
        self.assertIsInstance(result, bool, "verify user command permission : check instance")

    def test_27_verify_user_command_permission_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.verify_user_command_permission()

    def test_27_verify_user_command_permission_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.verify_user_command_permission(app_id=app_id, cmd="rm -rf")

    def test_28_get_app_health_check(self):
        app = self.__sample_app()

        result = self.__app.get_app_health_check(app_id=int(app["id"]))
        self.assertIsInstance(result, list, "get app health check : check instance")

    def test_28_get_app_health_check_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_health_check()

    def test_28_get_app_health_check_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_health_check(app_id=app_id)

    def test_29_add_app_health_check(self):
        app = self.__sample_app()

        result = self.__app.add_app_health_check(app_id=int(app["id"]), end_point="/ping", check_rate=0, schema="http",
                                                 initial_delay=10, response_code=200, response_string="Ok")
        self.assertIsInstance(result, list, "add app health check : check instance")

    def test_29_add_app_health_check_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.add_app_health_check()

    def test_29_add_app_health_check_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.add_app_health_check(app_id=app_id)

    def test_30_delete_all_app_health_checks(self):
        app = self.__sample_app()

        result = self.__app.delete_all_app_health_checks(app_id=int(app["id"]), path="/ping")
        self.assertIsInstance(result, list, "delete all app health checks : check instance")

    def test_30_delete_all_app_health_checks_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.delete_all_app_health_checks()

    def test_30_delete_all_app_health_checks_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.delete_all_app_health_checks(app_id=app_id, path="/ping")

    def test_31_update_health_check_by_id(self):
        app = self.__sample_app()
        health_list = self.__app.get_app_health_check(int(app["id"]))
        if len(health_list) == 0:
            self.skipTest("update health check by id : empty health check")

        result = self.__app.update_health_check_by_id(app_id=int(app["id"]), health_id=health_list[0]["id"],
                                                      end_point="/ping_edited", check_rate=0, schema="http",
                                                      initial_delay=10, response_code=200, response_string="Ok")
        self.assertIsInstance(result, dict, "update health check by id : check instance")

    def test_31_update_health_check_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.update_health_check_by_id()

    def test_31_update_health_check_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.update_health_check_by_id(app_id=app_id, health_id="456",
                                                 end_point="/ping_edited", check_rate="0", schema="http",
                                                 initial_delay="10", response_code="200", response_string="Ok")

    def test_32_delete_health_check_by_id(self):
        app = self.__sample_app()
        health_list = self.__app.get_app_health_check(int(app["id"]))
        if len(health_list) == 0:
            self.skipTest("delete health check by id : empty health check")

        result = self.__app.delete_health_check_by_id(app_id=int(app["id"]), health_id=health_list[0]["id"])
        self.assertIsInstance(result, dict, "delete health check by id : check instance")

    def test_32_delete_health_check_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.delete_health_check_by_id()

    def test_32_delete_health_check_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.delete_health_check_by_id(app_id=app_id, health_id="456")

    def test_33_get_real_time_app_logs_by_id(self):
        app = self.__sample_app()

        result = self.__app.get_real_time_app_logs_by_id(app_id=int(app["id"]), time=1584168044000)
        self.assertIsInstance(result, dict, "get real time app logs by id : check instance")

    def test_33_get_real_time_app_logs_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_real_time_app_logs_by_id()

    def test_33_get_real_time_app_logs_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_real_time_app_logs_by_id(app_id=app_id, time="123")

    def test_34_transfer_app_by_id(self):
        if self.__app_for_transfer is None:
            self.skipTest("transfer app by id : برنامه تستی برای انتقال ایجاد نشده")

        result = self.__app.transfer_app_by_id(app_id=int(self.__app_for_transfer["id"]),
                                               customer_email=COLLABORATOR_EMAIL, add_as_collaborator=False,
                                               transfer_git=False, transfer_image_repo=False)
        self.assertIsInstance(result, bool, "transfer app by id : check instance")

    def test_34_transfer_app_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.transfer_app_by_id()

    def test_34_transfer_app_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.transfer_app_by_id(app_id=app_id, customer_email="asdasd", add_as_collaborator="False",
                                          transfer_git="False", transfer_image_repo="False")

    def test_35_get_app_web_hooks(self):
        app = self.__sample_app()
        result = self.__app.get_app_web_hooks(app_id=int(app["id"]))
        self.assertIsInstance(result, list, "get app web hooks : check instance")

    def test_35_get_app_web_hooks_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_web_hooks()

    def test_35_get_app_web_hooks_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_web_hooks(app_id=app_id)

    def test_36_update_app_web_hook_by_id(self):
        app = self.__sample_app()
        web_hooks = self.__app.get_app_web_hooks(app_id=int(app["id"]))
        if len(web_hooks) == 0:
            self.skipTest("update app web hook by id : empty web hook")

        config = {
            "secured": True,
            "topics": Topics.ALL,
            "url": "https://karthing.ir/test.php?platform=sakku&updated_webhook=true"
        }

        result = self.__app.update_app_web_hook_by_id(app_id=int(app["id"]), web_hook_id=web_hooks[0]["id"],
                                                      config=config)
        self.assertIsInstance(result, dict, "update app web hook by id : check instance")

    def test_36_update_app_web_hook_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.update_app_web_hook_by_id()

    def test_36_update_app_web_hook_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.update_app_web_hook_by_id(app_id=app_id, web_hook_id="15", config="")

    def test_37_delete_app_web_hook_by_id(self):
        app = self.__sample_app()
        web_hooks = self.__app.get_app_web_hooks(app_id=int(app["id"]))

        if len(web_hooks) == 0:
            self.skipTest("delete app web hook by id : empty web hook")

        result = self.__app.delete_app_web_hook_by_id(app_id=int(app["id"]), web_hook_id=web_hooks[0]["id"])
        self.assertIsInstance(result, int, "delete app web hook by id : check instance")

    def test_37_delete_app_web_hook_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.delete_app_web_hook_by_id()

    def test_37_delete_app_web_hook_by_id_validation_error(self):
        app_id = "123465"
        with self.assertRaises(InvalidDataException):
            self.__app.delete_app_web_hook_by_id(app_id=app_id, web_hook_id="15")

    def test_38_get_app_by_name(self):
        result = self.__app.get_app_by_name(name="python")
        self.assertIsInstance(result, dict, "get app by name : check instance")

    def test_38_get_app_by_name_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_app_by_name()

    def test_38_get_app_by_name_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.get_app_by_name(name="")

    def test_39_create_app_by_docker_compose(self):
        self.__docker_compose_name = "group{}".format(datetime.now().__format__("%Y%m%d"))
        config = sample_app_config(name=self.__docker_compose_name)

        result = self.__app.create_app_by_docker_compose(compose_path=COMPOSE_PATH, global_config=config)
        print(result)
        self.assertIsInstance(result, list, "create app by docker compose : check instance")

    def test_39_create_app_by_docker_compose_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.create_app_by_docker_compose()

    def test_39_create_app_by_docker_compose_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.create_app_by_docker_compose(compose_path=123, global_config="")

    def test_40_get_group_with_name(self):
        result = self.__app.get_group_with_name(group_name=self.__docker_compose_name)
        self.assertIsInstance(result, dict, "get group with name : check instance")

    def test_40_get_group_with_name_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.get_group_with_name()

    def test_40_get_group_with_name_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.get_group_with_name(group_name="")

    def test_41_create_pipeline(self):
        configs = [sample_app_config(name="p1_{}".format(datetime.now().__format__("%Y%H%M%S"))),
                   sample_app_config(name="p2_{}".format(datetime.now().__format__("%Y%H%M%S")))]

        result = self.__app.create_pipeline(configs=configs)
        self.assertIsInstance(result, bool, "create pipeline : check instance")

    def test_41_create_pipeline_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.create_pipeline()

    def test_41_create_pipeline_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.create_pipeline(configs={})

    def test_42_create_app_by_machine_mechanism(self):
        name = "mm_{}".format(datetime.now().__format__("%Y%H%M%S"))
        result = self.__app.create_app_by_machine_mechanism(config=sample_app_config(name))
        self.assertIsInstance(result, dict, "create app by machine mechanism : check instance")

    def test_42_create_app_by_machine_mechanism_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.create_app_by_machine_mechanism()

    def test_42_create_app_by_machine_mechanism_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.create_app_by_machine_mechanism(config="")

    def test_43_get_user_apps_status_list(self):
        result = self.__app.get_user_apps_status_list()
        self.assertIsInstance(result, list, "get user apps status list : check instance")

    def test_43_get_user_apps_status_list_all_params(self):
        app = self.__sample_app()
        result = self.__app.get_user_apps_status_list(app_id=int(app["id"]))
        self.assertIsInstance(result, list, "get user apps status list : check instance")

    def test_43_get_user_apps_status_list_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.get_user_apps_status_list(app_id="123")

    def test_44_stop_app_deploy_with_queue_id(self):
        result = self.__app.stop_app_deploy_with_queue_id(deploy_queue_id="45645645")

        self.assertIsInstance(result, str, "stop app deploy with queue id : check instance")

    def test_44_stop_app_deploy_with_queue_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.stop_app_deploy_with_queue_id()

    def test_44_stop_app_deploy_with_queue_id_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__app.stop_app_deploy_with_queue_id(deploy_queue_id=123)

    def test_903_delete_app_by_id(self):
        app = self.__sample_app()

        result = self.__app.delete_app_by_id(app_id=int(app["id"]), force=True)

        self.assertIsInstance(result, dict, "delete app by id : check instance")

    def test_903_delete_app_by_id_required_params(self):
        with self.assertRaises(TypeError):
            self.__app.delete_app_by_id()

    def test_903_delete_app_by_id_validation_error(self):
        app_id = "123465"
        force = "True"
        with self.assertRaises(InvalidDataException):
            self.__app.delete_app_by_id(app_id=app_id, force=force)
