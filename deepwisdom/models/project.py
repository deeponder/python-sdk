import json
import os
import string
import time
import logging
from dataclasses import dataclass

import trafaret as t
import deepwisdom.errors as err

from deepwisdom._compat import Int, String

from .api_object import APIObject
from deepwisdom.enums import API_URL, PROJECT_DEFAULT_ADVANCE_SETTING
from .trial import Trial
from .solution import Solution
from .model import ModelInstance
from .dataset import PredictDataset
from deepwisdom.models.deployment import Deployment, DeploymentListMember, CreateDeployRequest
from deepwisdom.models.offline_predictions import OfflinePrediction, OfflinePredictionListMember

from typing import Optional, List
from copy import deepcopy


@dataclass
class TrainSetting(dict):
    train_data_ratio: int = 80
    training_program: string = "指标优先"
    call_limit: List[int] = None
    instance_num: int = 2
    call_delay: int = 50
    gpu_mem: int = 0
    memory_limit: int = 20
    max_trials: int = 30
    trial_concurrency: int = 3
    random_seed: int = 1647

    def __setattr__(self, k, v):
        if k in self.__dataclass_fields__:
            self[k] = v
        super().__setattr__(k, v)


@dataclass
class AdvanceSetting(dict):
    gp_switch: string = None
    optimizer: string = None
    random_seed: int = None
    target_train: TrainSetting = None

    def __setattr__(self, k, v):
        if k in self.__dataclass_fields__:
            self[k] = v
        super().__setattr__(k, v)


class Project(APIObject):
    """

    """
    _converter = t.Dict(
        {
            t.Key("id") >> "project_id": Int,
            t.Key("name"): String,
            t.Key("user_id"): Int,
            t.Key("modal_type", optional=True) >> "model_type": Int,
            t.Key("task_type"): Int,
            t.Key("description", optional=True): String(allow_blank=True),
            t.Key("status"): Int,

        }
    ).allow_extra("*")

    def __init__(
            self,
            project_id,
            name=None,
            user_id=None,
            model_type=None,
            task_type=None,
            description=None,
            status=None,
    ):
        """
        项目抽象类
        Args:
            project_id (int):
            name (str):
            user_id (int):
            model_type (int):
            task_type (int):
            description (str):
            status (int):
        """
        self.project_id = project_id
        self.name = name
        self.user_id = user_id
        self.model_type = model_type
        self.task_type = task_type
        self.description = description
        self.status = status

    @classmethod
    def create_from_dataset(
            cls,
            dataset_id,
            name=None,
            model_type=None,
            task_type=None,
            description=None,
            scene=None,
            primary_label=None,
            primary_main_time_col=None,
            id_cols=None,
            table_relation=None,
            advance_settings: Optional[AdvanceSetting] = None,
            search_space_id=1,
            icon='{"name": "IconBangong", "label": "办公"}'

    ):
        """
        从现有的数据集创建项目
        Args:
            dataset_id (int): 数据集id
            name (str): 项目名
            model_type (int): 模态类型。 0CSV,1VIDEO,2IMAGE,3SPEECH,4TEXT
            task_type (int): 任务类型。0二分类/分类,1多分类/检测/意图识别/匹配,2回归/定位/语音分离/序列,3时序/分隔
            description (str): 项目描述
            scene (int): 场景标签。 枚举
            primary_label (str):  预测列
            primary_main_time_col (str):  时间列
            id_cols (str): id列
            table_relation (str): 表关系
            advance_settings (AdvanceSetting): 高级
            search_space_id (int): 搜索空间id
            icon (str):

        Returns:
            Project
        """

        proj_data = {}
        proj_data["modal_type"] = model_type
        proj_data["name"] = "SDK_PROJ_" + str(dataset_id + time.time())
        if name is not None:
            proj_data["name"] = name

        proj_data["task_type"] = task_type
        # 任务描述
        proj_data["description"] = description

        proj_data["scene"] = scene
        proj_data["primary_label"] = primary_label
        proj_data["primary_main_time_col"] = primary_main_time_col
        proj_data["id_cols"] = id_cols
        proj_data["table_relation"] = json.dumps({"primary_table": dataset_id, "secondary_tables": []})

        settings = deepcopy(PROJECT_DEFAULT_ADVANCE_SETTING)
        advance_settings = advance_settings or {}
        settings.update(advance_settings)
        proj_data["advance_settings"] = json.dumps(settings)
        proj_data["search_space_id"] = search_space_id
        proj_data["icon"] = icon

        resp = cls._client._post(API_URL.PROJECT_CREATE, proj_data)
        if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
            raise err.ServerError(resp, resp["code"])

        proj_id = resp["data"]["new_project_info"][0]["id"]
        data = {
            "project_id": proj_id
        }
        server_data = cls._server_data(API_URL.PROJECT_INFO, data)
        return cls.from_server_data(server_data)

    @classmethod
    def create_from_id(cls, proj_id: int):
        """
        直接从项目id创建项目对象
        Args:
            proj_id (int):

        Returns:

        """

        data = {
            "project_id": proj_id
        }
        server_data = cls._server_data(API_URL.PROJECT_INFO, data)
        return cls.from_server_data(server_data)

    @classmethod
    def delete(cls, proj_ids: list):
        """

        Args:
            proj_ids (list):

        Returns:

        """

        data = {
            "project_id": proj_ids
        }

        cls._client._delete(API_URL.PROJECT_DELETE, data)

    def update_advance_settings(self, advance_settings: Optional[AdvanceSetting]):
        """
        项目高级设置更新
        Returns:

        """

        settings = deepcopy(PROJECT_DEFAULT_ADVANCE_SETTING)
        advance_settings = advance_settings or {}
        settings.update(advance_settings)

        data = {
            "project_id": self.project_id,
            "advance_settings": json.dumps(settings)
        }

        self._client._patch(API_URL.PROJECT_ADVANCESETTING_UPDATE, data)

    def train(self):
        """
        开始训练
        Returns:

        """
        data = {
            "project_id": self.project_id
        }
        self._client._post(API_URL.PROJECT_TRAIN, data)

        return

    def wait_train(self):
        """
        训练，并等待训练完成
        Returns:

        """
        self.train()

        # 轮询查询训练进度, 5s一次
        while True:

            data = {
                "project_id": self.project_id
            }
            server_data = self._server_data(API_URL.PROJECT_INFO, data)
            logging.info(server_data)

            if "ret" in server_data and server_data["ret"] != 1:
                logging.error(server_data)
                raise err.GetProjectInfoError
            # 训练成功
            if server_data["status"] == 2:
                self.status = server_data["status"]
                break

            # 训练失败
            if server_data["status"] == 3:
                raise err.ProjectTrainError

            time.sleep(5)

        return

    def check_train_finish(self):
        """
        检查训练是否完成
        Returns:
            True:完成
            False: 未完成
        """

        data = {
            "project_id": self.project_id
        }
        server_data = self._server_data(API_URL.PROJECT_INFO, data)
        logging.info(server_data)

        if "ret" in server_data and server_data["ret"] != 1:
            logging.error(server_data)
            raise err.GetProjectInfoError
        # 训练成功
        if server_data["status"] == 2:
            return True

        # 训练失败
        if server_data["status"] == 3:
            raise err.ProjectTrainError

        return False

    def retrain(self):
        """
        重新训练
        Returns:

        """

        data = {
            "project_id": self.project_id
        }
        self._client._patch(API_URL.PROJECT_TRAIN, data)

    def terminate_train(self):
        """
        终止训练， /project/terminate/train
        Returns:

        """
        data = {
            "project_id": self.project_id
        }
        self._client._post(API_URL.PROJECT_TERMINATE_TRAIN, data)

    def dataset_list(self):
        """
        项目绑定的数据集列表
        Returns:

        """

        data = {
            "project_id": self.project_id
        }

        server_data = self._server_data(API_URL.PROJECT_DATASET_LIST, data)
        return server_data

    def model_list(self):
        """

        Returns:

        """

    def trial_list(self):
        """
        获取项目的实验列表
        Returns:
            []Trial
        """
        data = {
            "project_id": self.project_id
        }
        server_data = self._server_data(API_URL.PROJECT_EFFECT, data)
        trials = server_data["scheme_data"]
        init_data = [dict(Trial._safe_data(item)) for item in trials]
        return [Trial(project_id=self.project_id, **data) for data in init_data]

    def service_list(self) -> List[DeploymentListMember]:
        """
        获取项目的服务列表
        Returns:
            List[DeploymentInfo]: 服务列表
        """
        data = {
            "project_id": self.project_id
        }
        server_data = self._server_data(API_URL.DEPLOY_LIST_DEPLOYMENTS, data)
        init_data = [DeploymentListMember._filter_data(DeploymentListMember._converter.check(item)) for item in
                     server_data]
        return [DeploymentListMember(**data) for data in init_data]

    def offline_prediction_list(self) -> List[OfflinePredictionListMember]:
        """获取项目的预测列表
        Args:
            project_id (uint64): 项目id

        """
        data = {
            "project_id": self.project_id,
        }

        server_data = self._server_data(API_URL.PREDICTION_LIST, data)
        init_data = [OfflinePredictionListMember._filter_data(OfflinePredictionListMember._converter.check(item)) for
                     item in server_data]
        return [OfflinePredictionListMember(**data) for data in init_data]

    def recommended_select_model(self):
        """
        获取推荐的模型
        Returns:
            ModelInstance
        """

        solutions = self.solution_list()
        try:
            models = self.get_select_models(solutions[0].trial_no, solutions[0].trial_type)
            return models[0]
        except IndexError:
            logging.error("no found")

        return None

    def solution_list(self):
        """
        项目方案列表
        Returns:
            []Solution
        """

        data = {
            "project_id": self.project_id
        }
        server_data = self._server_data(API_URL.PROJECT_SCHEME, data)
        solution_list = server_data["scheme"]
        init_data = [dict(Solution._safe_data(item)) for item in solution_list]
        return [Solution(project_id=self.project_id, **data) for data in init_data]

    def get_select_models(self, trial_no: int, trial_type: int):
        """
        需要部署的模型信息
        Args:
            trial_no (int):
            trial_type (int):

        Returns:
            []ModelInstance
        """

        data = {
            "project_id": self.project_id,
            "trial_no": trial_no,
            "trial_type": trial_type
        }

        server_data = self._server_data(API_URL.PROJECT_MODEL_SELECT, data)
        init_data = [dict(ModelInstance._safe_data(item)) for item in server_data]
        return [ModelInstance(project_id=self.project_id, trial_no=trial_no, trial_type=trial_type, **data)
                for data in init_data]

    def upload_predict_dataset(self, filename=None):
        """

        Args:
            filename (str):

        Returns:

        """
        data = {
            "project_id": self.project_id
        }

        file_type = os.path.splitext(filename)[-1][1:]
        if file_type == "csv" or file_type == "txt":
            mime_type = 'text/csv'
        else:
            mime_type = 'application/octet-stream'
        with open(filename, 'rb') as f:
            files = {
                "file": (os.path.basename(filename), f, mime_type)
            }

            response = self._client._upload(API_URL.DATASET_PREDICT_UPLOAD, data, files)

        dataset = dict(PredictDataset._safe_data(response["data"]))
        return PredictDataset(project_id=self.project_id, **dataset)

    def predict_dataset_list(self):
        """
        离线预测数据集列表
        Returns:

        """
        data = {
            "project_id": self.project_id
        }

        server_data = self._server_data(API_URL.DATASET_PREDICT_LIST, data)

        init_data = [dict(PredictDataset._safe_data(item)) for item in server_data]
        return [PredictDataset(project_id=self.project_id, **data) for data in init_data]

    def predict_file(self, model_id: int, filename) -> OfflinePrediction:
        """预测文件

        Returns:
            OfflinePrediction: 离线预测对象
        """
        dataset = self.upload_predict_dataset(filename)
        if not dataset:
            return None
        prediction = OfflinePrediction.predict(model_id, dataset.dataset_id)
        return prediction

    def create_service(self, model_id: int, service_name: str, gpu_mem: int, mem: int, min_pod: int,
                       max_pod: int) -> Deployment:
        req = CreateDeployRequest(self.project_id, model_id, service_name, gpu_mem, mem, min_pod, max_pod)
        return Deployment.create_deployment(req)


class TableRelation(object):
    """

    """

    def __init__(
            self,
            pri_dataset_id=None,
            sec_dataset_id=None,
            main_col=None,
            main_col_type=None,
            relation_col=None,
            relation_col_type=None
    ):
        self.pri_dataset_id = pri_dataset_id
        self.sec_dataset_id = sec_dataset_id
        self.main_col = main_col
        self.main_col_type = main_col_type
        self.relation_col = relation_col
        self.relation_col_type = relation_col_type
