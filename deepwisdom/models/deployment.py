# -*- coding: utf-8 -*-
"""
天机SDK-Python
推理服务部署
"""
from typing import List
from urllib import parse
from .api_object import APIObject
from deepwisdom.enums import API_URL


class CreateDeployRequest(object):
    project_id: int = 0  # 项目id
    model_inst_id: int = 0  # 模型id
    name: str = ''  # 服务名
    gpu_num: int = 0  # gpu数量
    gpu_mem: int = 0  # gpu显存限制MB
    memory_limit: int = 0  # MB 内存限制
    max_pod: int = 0  # 最大pod数
    min_pod: int = 0  # 最少pod数

    def __init__(self, project_id, model_inst_id, name, gpu_num, gpu_mem, memory_limit, max_pod, min_pod):
        self.project_id = project_id
        self.model_inst_id = model_inst_id
        self.name = name
        self.gpu_num = gpu_num
        self.gpu_mem = gpu_mem
        self.memory_limit = memory_limit
        self.max_pod = max_pod
        self.min_pod = min_pod


class DeploymentInfo(object):
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


class Deployment(APIObject):

    @classmethod
    def create_deployment(cls, options: CreateDeployRequest):
        """创建服务

        Args:
            options (CreateDeployRequest): 服务创建请求参数

        Returns:
            [type]: [description]
        """
        data = {}
        data.update(options)
        rsp = cls._client._post(API_URL.DEPLOY_CREATE_SERVICE, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def get_deployment_detail(cls, service_id, **kwargs) -> DeploymentInfo:
        """获取服务详情

        Args:
            service_id (int): 服务id
        Returns:
            DeploymentInfo: 服务详情
        """
        data = {
            "service_id": service_id
        }
        rsp = cls._client._get(API_URL.DEPLOY_GET_SERVICE_DETAIL, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def list_deployments(cls, project_id: int, **kwargs) -> List[DeploymentInfo]:
        """获取服务部署列表

        Args:
            project_id (int): 项目id

        Returns:
            List[DeploymentInfo]: 服务列表
        """
        data = {
            "project_id": project_id
        }
        rsp = cls._client._get(API_URL.DEPLOY_LIST_DEPLOYMENTS, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def resident_deployment(cls, svc_id: int, min_pod: int):
        """切换服务常驻状态

        Args:
            svc_id (int64): 服务id
            min_pod (int): 最少pod数，大于0为服务常驻，等于0为非常驻
        """
        data = {
            "svc_id": svc_id,
            "min_pod": min_pod
        }
        rsp = cls._client._post(API_URL.DEPLOY_RESIDENT_DEPLOYMENT, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def delete_deployments(cls, service_ids: List[int]):
        """删除服务

        Args:
            service_ids (int64): 服务id
        """
        data = {
            "svc_ids": service_ids
        }
        rsp = cls._client._delete(API_URL.DEPLOY_DELETE_DEPLOYMENT, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def rename_deployment(cls, svc_id: int, svc_name: str):
        """重命名服务

        Args:
            svc_id (int): 服务id
            svc_name (str): 新服务名称
        """
        data = {
            "svc_id": svc_id,
            "svc_name": svc_name
        }
        rsp = cls._client._patch(API_URL.DEPLOY_RENAME_DEPLOYMENT, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def get_deployment_log(cls, svc_id: int) -> str:
        """获取服务日志

        Args:
            svc_id (int): 服务id

        Returns:
            str: 日志内容
        """
        data = {
            "service_id": svc_id
        }
        rsp = cls._client._get(API_URL.DEPLOY_GET_DEPLOYMENT_LOG, data)
        if "data" in rsp:
            return rsp['data']
        return None
