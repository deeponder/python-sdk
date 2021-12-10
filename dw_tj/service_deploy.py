# -*- coding: utf-8 -*-
"""
天机SDK-Python
推理服务部署
"""
from typing import List

from .base import DwTjBase


class CreateDeployRequest():
    project_id: int = 0  # 项目id
    model_inst_id: int = 0  # 模型id
    name: str = ''  # 服务名
    gpu_num: int = 0  # gpu数量
    gpu_mem: int = 0  # gpu显存限制MB
    memory_limit: int = 0  # MB 内存限制
    max_pod: int = 0  # 最大pod数
    min_pod: int = 0  # 最少pod数


class DeploymentInfo():
    id: int = 0
    project_id: int = 0
    user_id: int = 0
    name: str = ''  # 服务中文名
    service_name: str = ''  # 服务名称-英文
    model_inst_id: int = 0  # 模型id
    serverless_infer_id: int = 0  # 服务部署id
    infer_task_id: int = 0
    deploy_model: str = ''  # 部署模型名称
    route_path: str = ''  # 服务调用URL
    token: str = ''  # 服务调用token
    status: int = 0
    infer_lock: int = 0
    min_pod: int = 0
    max_pod: int = 0
    create_time: str = ''  # 2021-10-27 18:43:12
    update_time: str = ''  # 2021-10-27 18:43:12
    deploy_time: str = ''  # 2021-10-27 18:43:12
    is_del: int = 0


class Deployment(DwTjBase):
    __create_service = '/sdk/sdksvr/datasetprepare'
    __get_service_detail = '/sdk/sdksvr/fileupload'
    __list_deployments = '/sdk/sdksvr/datasetupload'
    __resident_deployment = '/api/v1/infer/resident'  # 推理服务常驻
    __rename_deployment = ''
    __delete_deployment = ''
    __get_deployment_log = ''

    def create_deployment(self, options: CreateDeployRequest):
        """创建服务

        Args:
            options (CreateDeployRequest): 服务创建请求参数

        Returns:
            [type]: [description]
        """
        data = {}
        data.update(options)
        return self._request("POST", self.__create_service, data)

    def get_deployment_detail(self, service_id, **kwargs) -> DeploymentInfo:
        """获取服务详情

        Args:
            service_id (int): 服务id
        Returns:
            DeploymentInfo: 服务详情
        """
        data = {
            "service_id": service_id
        }
        return self._request("POST", self.__get_service_detail, data)

    def list_deployments(self, project_id: int, **kwargs) -> List[DeploymentInfo]:
        """获取服务部署列表

        Args:
            project_id (int): 项目id

        Returns:
            List[DeploymentInfo]: 服务列表
        """
        data = {
            "project_id": project_id
        }
        return self._request("POST", self.__list_deployments, data)

    def resident_deployment(self, svc_id: int, min_pod: int):
        """切换服务常驻状态

        Args:
            svc_id (int64): 服务id
            min_pod (int): 最少pod数，大于0为服务常驻，等于0为非常驻
        """
        data = {
            "svc_id": svc_id,
            "min_pod": min_pod
        }
        return self._request("POST", self.__resident_deployment, data)

    def delete_deployments(self, service_ids: List[int]):
        """删除服务

        Args:
            service_id (int64): 服务id
        """
        data = {
            "svc_ids": service_ids
        }
        return self._request("DELETE", self.__delete_deployment, data)

    def rename_deployment(self, svc_id: int, svc_name: str):
        """重命名服务

        Args:
            svc_id (int): 服务id
            svc_name (str): 新服务名称
        """
        data = {
            "svc_id": svc_id,
            "svc_name": svc_name
        }
        return self._request("PATCH", self.__rename_deployment, data)

    def get_deployment_log(self, svc_id: int) -> str:
        """获取服务日志

        Args:
            svc_id (int): 服务id

        Returns:
            str: 日志内容
        """
        data = {
            "service_id": svc_id
        }
        return self._request("GET", self.__get_deployment_log, data)
