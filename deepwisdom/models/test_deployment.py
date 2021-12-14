import json
from unittest import TestCase
from deepwisdom.models import Deployment


class TestDeployment(TestCase):
    def test_create_deployment(self):
        deploy = Deployment.create_deployment({
            "project_id": 3976,
            "model_inst_id": 6113,
            "name": "灵魂拷问--晚上吃什么",
            "gpu_num": 1,
            "gpu_mem": 2,
            "memory_limit": 2,
            "min_pod": 1,
            "max_pod": 2,
        })
        print(deploy)

    def test_get_deployment_detail(self):
        deploy = Deployment.get_deployment_detail(480)
        print(json.dumps(deploy))

    def test_list_deployments(self):
        deploy = Deployment.list_deployments(3976)
        print(deploy)

    def test_resident_deployment(self):
        deploy = Deployment.resident_deployment(480, 2)
        print(deploy)

    def test_delete_deployments(self):
        deploy = Deployment.delete_deployments([480])
        print(deploy)

    def test_rename_deployment(self):
        deploy = Deployment.rename_deployment(480, "猪八戒吃了唐僧")
        print(deploy)

    def test_get_deployment_log(self):
        deploy = Deployment.delete_deployments(480)
        print(deploy)