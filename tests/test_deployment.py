import json
from unittest import TestCase
from deepwisdom.models import Deployment

deploy_id = 480


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
        self.assertEqual(deploy.project_id, 3976)
        print(deploy)

    def test_get_deployment_detail(self):
        deploy = Deployment.get_deployment_detail(deploy_id)
        self.assertEqual(deploy.id, deploy_id)
        self.assertEqual(deploy.project_id, 3976)
        print(deploy.status)

    def test_list_deployments(self):
        deploys = Deployment.list_deployments(3976)
        for deploy in deploys:
            detail = deploy.get_deployment_detail()
            self.assertEqual(detail.name, deploy.service_name)
        print(deploys)

    def test_resident_deployment(self):
        deploy = Deployment.resident_deployment(deploy_id, 2)
        self.assertEqual(deploy.min_pod, 2)
        print(deploy)

    def test_delete_deployments(self):
        deploy = Deployment.delete_deployments([deploy_id])
        self.assertEqual(deploy, True)
        print(deploy)

    def test_rename_deployment(self):
        deploy = Deployment.rename_deployment(deploy_id, "猪八戒吃了唐僧")
        self.assertEqual(deploy.name, "猪八戒吃了唐僧")
        print(deploy)

    def test_get_deployment_log(self):
        deploy = Deployment.delete_deployments(deploy_id)
        print(deploy)

    def test_get_service(self):
        deploy = Deployment.get_service(deploy_id)
        print(deploy.status)
        print(deploy.get_service_status(deploy_id))

    def test_call_service(self):
        deploy = Deployment.get_service(deploy_id)
        print(deploy.call_service({}))

    def test_get_service_api(self):
        deploy = Deployment.get_service_api(deploy_id)
        print(deploy)
