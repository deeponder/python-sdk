import hashlib
import json
import logging
import os
import time
from io import BytesIO

import trafaret as t
import deepwisdom.errors as err

from deepwisdom._compat import Int, String
from .api_object import APIObject
from deepwisdom.enums import API_URL



def _get_upload_id(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            data = f.read()
            return hashlib.md5(data).hexdigest() + "-" + str(time.time())
    else:
        logging.error("%s doesn't exist, no md5", file_path)
        return ""


_base_dataset_schema = t.Dict(
    {
        t.Key("id") >> "dataset_id": Int,
        t.Key("file_name"): String,
        t.Key("create_time"): String,
        t.Key("file_size"): Int,
        t.Key("file_type"): Int,
    }
)

class Dataset(APIObject):
    """
    
    """
    _converter = _base_dataset_schema.allow_extra("*")

    def __init__(
        self,
        dataset_id,
        file_name=None,
        create_time=None,
        file_size=None,
        file_type=None

    ):
        self.dataset_id = dataset_id
        self.name = file_name
        self.create_time = create_time
        self.file_size = file_size
        self.file_type = file_type

    @classmethod
    def create_from_file(
        cls,
        filename=None,
        model_type=None,
        annotation_type=1,
        dataset_scene_id=1,
        sep="\\t",
        max_chunk_size=10*1024*1024
    ):
        """

        :param filename:
        :param model_type:
        :param annotation_type:
        :param dataset_scene_id:
        :param sep:
        :param max_chunk_size:
        :return:
        """
        dataset_id, msg = cls.dataset_upload(filename, model_type, annotation_type,
                                             dataset_scene_id, sep, max_chunk_size)
        if dataset_id < 0:
            logging.info(msg)
            raise err.UploadTrainDataError

        data = {
            "dataset_id": dataset_id
        }
        server_data = cls._server_data(API_URL.DATASET_INFO, data)

        return cls.from_server_data(server_data)

    @classmethod
    def _file_upload(cls, url, file, data):
        return cls._client._upload(url, data, file)

    @classmethod
    def dataset_upload(
        cls,
        file_path,
        model_type,
        annotation_type,
        dataset_scene_id,
        sep,
        max_chunk_size
    ):
        upload_id = _get_upload_id(file_path)
        if upload_id == "":
            return -1, file_path + " doesn't exist"
        # file_path = filepath.replace('\\', '/')
        file_names = os.path.split(file_path)
        filename = file_names[-1]
        # 上传准备
        prepare_data = {}
        prepare_data["modal_type"] = model_type
        prepare_data["filename"] = filename

        prepare_data["upload_id"] = upload_id

        resp = cls._client._post(API_URL.DATASET_PREPARE, prepare_data)

        if resp["data"]["ret"] != 1:
            return -1, resp

        _chunk_id_list = resp["data"]["chunk_id_list"]
        chunk_id_list = list()

        # 文件上传
        with open(file_path, 'rb') as fp:
            while 1:
                chunk = fp.read(max_chunk_size)
                if not chunk:
                    break
                chunk_id = hashlib.md5(chunk).hexdigest()
                chunk_id_list.append(chunk_id)
                if chunk_id in _chunk_id_list:
                    continue
                uploadData = {}
                uploadData["upload_id"] = upload_id
                uploadData["chunk_id"] = chunk_id
                chunk_fp = BytesIO(chunk)
                files = {
                    "file": (chunk_id, chunk_fp, 'application/octet-stream')
                }
                resp = cls._file_upload(API_URL.FILE_UPLOAD, files, uploadData)
                chunk_fp.close()
                if resp["data"]["ret"] != 1:
                    return -1, resp

        # 数据集上传
        dataset_deal_data = {}

        dataset_deal_data["filename"] = filename
        dataset_deal_data["upload_id"] = upload_id
        dataset_deal_data["chunk_id_list"] = json.dumps(chunk_id_list)
        dataset_deal_data["modal_type"] = model_type
        dataset_deal_data["sep"] = sep
        dataset_deal_data["annotation_type"] = annotation_type
        # 场景Id， 二分等
        dataset_deal_data["dataset_scene_id"] = dataset_scene_id

        resp = cls._client._post(API_URL.DATASET_UPLOAD, dataset_deal_data)

        if resp["data"]["ret"] != 1:
            return -1, resp

        # 3秒间隔，轮询获取
        # 获取数据集信息
        while True:
            dataset_query_data = {}
            dataset_query_data["upload_id"] = upload_id

            resp = cls._client._post(API_URL.DATASET_QUERY, dataset_query_data)
            logging.info(resp)
            if resp["errNo"] != 0 or resp["data"]["data_set_id"] == -1:
                return -1, resp

            # id不为0生成完成
            if resp["data"]["data_set_id"] > 0:
                return resp["data"]["data_set_id"], "success"

            time.sleep(3)
