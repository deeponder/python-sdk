import json
from unittest import TestCase
from deepwisdom.models import Deployment
from deepwisdom.models.deployment import CreateDeployRequest

deploy_id = 480


class TestDeployment(TestCase):
    def test_create_deployment(self):
        req = CreateDeployRequest(3973, 6185, "魂拷问--晚上吃什么", 2, 3, 1, 1)
        deploy = Deployment.create_deployment(req)
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
            # detail.delete_deployments([detail.id])
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
        deploy = Deployment.get_service(530)
        print(deploy.status)
        print(deploy.get_service_status())

    def test_call_service(self):
        deploy = Deployment.get_service(546)
        rsp = deploy.call_service({})
        print(rsp)

    def test_get_service_api(self):
        deploy = Deployment.get_service_api(deploy_id)
        print(deploy)
