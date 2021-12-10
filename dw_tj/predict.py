# -*- coding: utf-8 -*-
"""
天机SDK-Python
模型数据集预测
"""
from typing import Any
from typing import List

from .base import DwTjBase


class PredictionItem(object):
    offline_id: int = 0
    offline_status: int = 0
    dataset_name: str = ''
    dataset_id: int = 0
    model_inst_id: int = 0


class OfflinePrediction(DwTjBase):
    __predict = '/sdk/sdksvr/projeval'
    __list_prediction = ''
    __delete_predictions = ''
    __get_predict_detail = ''
    __dataset_download = ''
    __result_download = ''

    def list_predictions(self, project_id: int) -> List[PredictionItem]:
        """获取预测列表
        Args:
            project_id (uint64): 项目id

        """
        data = {
            "project_id": project_id,
        }

        return self._request("GET", self.__list_prediction, data)

    def predict(self, model_inst_id: int, dataset_id: int) -> Any:
        """开始离线预测
            http://yapi.deepwisdomai.com/project/11/interface/api/242

        Args:
            model_inst_id (int64): 该项目对应的模型实例id
            dataset_id (int64): 用于离线预测的数据集id
        """
        data = {
            "model_inst_id": model_inst_id,
            "dataset_id": dataset_id,
        }
        return self._request("POST", self.__predict, data)

    def get_predict_detail(self, offline_id: int):
        """获取离线预测详情

        Args:
            offline_id (int64): 离线预测id
        """
        data = {
            "offline_id": offline_id,
        }
        return self._request("GET", self.__get_predict_detail, data)

    def result_download(self, project_id: int):
        """项目预测报告下载

        Args:
            project_id (int64):  项目id
        """
        data = {
            "project_id": project_id,
        }
        return self._request("GET", self.__result_download, data)

    def dataset_download(self, offline_id: int, target_cols: List[str] = []):
        """离线预测数据集下载

        Args:
            offline_id (int): 预测数据集id
            target_cols (List[str]): 数据列选择,默认为空[]

        Returns:
            str: 数据集地址
        """
        data = {
            "offline_id": offline_id,
            "dataset_id": target_cols,
        }
        return self._request("POST", self.__dataset_download, data)

    def delete_predictions(self, offline_ids: List[int]):
        """批量删除预测
            http://yapi.deepwisdomai.com/project/11/interface/api/2842
        Args:
            offline_ids (List[int]): 离线预测id数组
        """
        data = {
            "offline_ids": offline_ids
        }
        return self._request("POST", self.__delete_predictions, data)
