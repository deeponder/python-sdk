# -*- coding: utf-8 -*-
"""
天机SDK-Python
模型数据集预测
"""
from typing import Any
from typing import List

from .api_object import APIObject
from deepwisdom.enums import API_URL


class PredictionItem(object):
    offline_id: int = 0
    offline_status: int = 0
    dataset_name: str = ''
    dataset_id: int = 0
    model_inst_id: int = 0


class OfflinePrediction(APIObject):
    @classmethod
    def list_predictions(cls, project_id: int) -> List[PredictionItem]:
        """获取预测列表
        Args:
            project_id (uint64): 项目id

        """
        data = {
            "project_id": project_id,
        }

        rsp = cls._client._get(API_URL.PREDICTION_LIST, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def predict(cls, model_inst_id: int, dataset_id: int) -> Any:
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
        rsp = cls._client._post(API_URL.PREDICTION_PREDICT, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def get_predict_detail(cls, offline_id: int):
        """获取离线预测详情

        Args:
            offline_id (int64): 离线预测id
        """
        data = {
            "offline_id": offline_id,
        }
        rsp = cls._client._get(API_URL.PREDICTION_DETAIL, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def result_download(cls, project_id: int, target_path: str):
        """项目预测报告下载,当前由前端渲染后下载，暂时不支持服务端直接下载 TODO

        Args:
            project_id (int64):  项目id
        """
        data = {
            "project_id": project_id,
        }
        rsp = cls._client._get(API_URL.PREDICTION_RESULT_DOWNLOAD, data)
        if "data" in rsp and "zip_name" in rsp["data"]:
            print(rsp)
            report = cls._client._get(rsp['data']["zip_name"], {})
            out = open(target_path, "w+")
            out.write(report)
            out.close()
        return None

    @classmethod
    def dataset_download(cls, offline_id: int, target_path: str, target_cols: List[str] = []):
        """离线预测数据集下载，暂时不可用 TODO

        Args:
            offline_id (int): 预测数据集id
            target_path (str): 下载路径
            target_cols (List[str]): 数据列选择,默认为空[]

        Returns:
            str: 数据集地址
        """
        data = {
            "offline_id": offline_id,
            "dataset_id": target_cols,
        }
        rsp = cls._client._get(API_URL.PREDICTION_DATASET_DOWNLOAD, data)
        if "data" in rsp:
            # pass
            # return rsp['data']
            fi = cls._client._get(cls.join_dataset_download_path(rsp['data']), {})
            out = open(target_path, "w+")
            out.write(fi)
            out.close()
        return None

    @classmethod
    def delete_predictions(cls, offline_ids: List[int]):
        """批量删除预测
            http://yapi.deepwisdomai.com/project/11/interface/api/2842
        Args:
            offline_ids (List[int]): 离线预测id数组
        """
        data = {
            "offline_ids": offline_ids
        }
        rsp = cls._client._post(API_URL.PREDICTION_DELETE, data)
        if "data" in rsp:
            return rsp['data']
        return None

    @classmethod
    def join_dataset_download_path(cls, path):
        return API_URL.DATASET_DOWNLOAD_HOST + path
