
# -*- coding: utf-8 -*-
"""
天机SDK-Python
"""
from io import BytesIO
import logging
import time

from .base import DwTjBase
from threading import Timer
import hashlib
import os
import json

class DwTj(DwTjBase) :
    __datasetPrepare = '/sdk/sdksvr/datasetprepare'
    __fileUpload = '/sdk/sdksvr/fileupload'
    __datasetUpload = '/sdk/sdksvr/datasetupload'
    __datasetInfo = '/sdk/sdksvr/querydataset'

    __getSvrList = '/sdk/sdksvr/svrlist'
    __getDataSets = '/sdk/sdksvr/datasetlist'
    __createProj = '/sdk/sdksvr/createproj'
    __projTrain = '/sdk/sdksvr/projtrain'
    __projReTrain = '/sdk/sdksvr/projretrain'
    __projInfo = '/sdk/sdksvr/projinfo'
    __projTrainResult = '/sdk/sdksvr/trainresult'
    __trainModelInfo ='/sdk/sdksvr/trainmodelinfo'
    __projEval = '/sdk/sdksvr/projeval'
    __inferSvr = '/sdk/sdksvr/infersvr'
    __svrOpt = '/sdk/sdksvr/svropt'

    __projAdvanceSetting = '/sdk/sdksvr/projadvancesetting'

    def getUploadId(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                data = f.read()
                return hashlib.md5(data).hexdigest() + "-" + str(time.time())
        else:
            logging.error("%s doesn't exist, no md5", file_path)
            return ""

    def getSvrList(self, options=None):
        """
            拉取服务列表
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("GET", self.__getSvrList, data)

    def datasetPrepare(self, options=None):
        """
            数据集上传准备
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("POST", self.__datasetPrepare, data)

    def fileUpload(self, files, options=None):
        """
        数据集文件上传
        :param options:
        :param url:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._upload(self.__fileUpload, data, files)

    def datasetUpload(self, options=None):
        """
            数据集上传
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("POST", self.__datasetUpload, data)

    def datasetInfo(self, options=None):
        """
            获取数据集id
        """
        options = options or {}

        # 请求数据
        data = {}

        data.update(options)

        return self._request("POST", self.__datasetInfo, data)

    def getDataSets(self, options=None):
        """
        拉取数据集列表
        :param options:
        :param url:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="
        data["dataset_name"] = ""

        data.update(options)

        return self._request("GET", self.__getDataSets, data)

    def createProj(self, options=None):
        """
        创建项目
        :param options:
        :param url:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        # print(data)
        return self._request("POST", self.__createProj, data)

    def projTrain(self, options=None):
        """
        开始训练
        :param options:
        :param url:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("POST", self.__projTrain, data)

    def projReTrain(self, options=None):
        """
        开始训练
        :param options:
        :param url:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("PATCH", self.__projReTrain, data)

    def projInfo(self, options=None):
        """
        训练进度/项目信息
        :param options:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("GET", self.__projInfo, data)

    def projTrainResult(self, options=None):
        """
        训练结果
        :param options:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        # 0 效果最优；1耗时最短
        data["schema_type"] = 0
        data.update(options)

        return self._request("GET", self.__projTrainResult, data)

    def trainModeInfo(self, options=None):
        """
        训练结果对应的模型信息获取（id等）
        :param options:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("GET", self.__trainModelInfo, data)

    def projEval(self, options=None):
        """
        离线验证
        :param options:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("POST", self.__projEval, data)

    def inferSvr(self, options=None):
        """
        创建推理服务
        :param options:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="


        # data["dataset_id"] = 3573
        data.update(options)

        return self._request("POST", self.__inferSvr, data)

    def svrOpt(self, options=None):
        """
        启停推理服务
        :param options:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="


        # data["dataset_id"] = 3573
        data.update(options)

        return self._request("POST", self.__svrOpt, data)

    def projAdvanceSetting(self, options=None):
        """
        启停推理服务
        :param options:
        :return:
        """
        options = options or {}

        # 请求数据
        data = {}
        data["bcode"] = "autotable"
        data["token"] = "Hy+b55u4C9KE8GSKEJ5xhw=="

        data.update(options)

        return self._request("PATCH", self.__projAdvanceSetting, data)

    def dataUpload(self, filepath, modal_type, annotation_type=1, dataset_scene_id=1, sep="\\t", max_chunk_size = 10*1024*1024):
        """
        数据集上传封装
        :param filepath: 数据集绝对路径
        :param modal_type: 模态类型。 0CSV,1VIDEO,2IMAGE,3SPEECH,4TEXT
        :param annotation_type: 标注类型。默认已标注1
        :param dataset_scene_id: 场景id。默认1 枚举
        :param seq: 表格分隔符。 枚举
        :return: 数据集id, msg
        """
        # 参数校验
        if modal_type not in [0, 1, 2, 3, 4]:
            return -1, "modal_type not support."
        if annotation_type not in [0, 1, 2, 3]:
            return -1, "annotation_type not support."

        upload_id = self.getUploadId(filepath)
        if upload_id == "":
            return -1, filepath + " doesn't exist"
        # file_path = filepath.replace('\\', '/')
        file_names = os.path.split(filepath)
        filename = file_names[-1]
        # 上传准备
        prepareData = {}
        prepareData["modal_type"] = modal_type
        prepareData["filename"] = filename

        
        prepareData["upload_id"] = upload_id

        resp = self.datasetPrepare(prepareData)
        logging.info(resp)

        if resp["data"]["ret"] != 1:
            return -1, resp
        _chunk_id_list = resp["data"]["chunk_id_list"]
        chunk_id_list = list()

        # 文件上传
        with open(filepath, 'rb') as fp:
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
                resp = self.fileUpload(files, uploadData)
                chunk_fp.close()
                if resp["data"]["ret"] != 1:
                    return -1, resp
        # 数据集上传
        datasetDealData = {}

        datasetDealData["filename"] = filename
        datasetDealData["upload_id"] = upload_id
        datasetDealData["chunk_id_list"] = json.dumps(chunk_id_list)
        datasetDealData["modal_type"] = modal_type
        datasetDealData["sep"] = sep
        datasetDealData["annotation_type"] = annotation_type
        # 场景Id， 二分等
        datasetDealData["dataset_scene_id"] = dataset_scene_id

        resp = self.datasetUpload(datasetDealData)
        logging.info(resp)
        if resp["data"]["ret"] != 1:
            return -1, resp

        # 3秒间隔，轮询获取
        # 获取数据集信息
        while True:
            datasetInfoData = {}
            datasetInfoData["upload_id"] = upload_id

            resp = self.datasetInfo(datasetInfoData)
            logging.info(resp)
            if resp["errNo"] != 0 or resp["data"]["data_set_id"]==-1:
                return -1, resp

            # id不为0生成完成
            if resp["data"]["data_set_id"] > 0:
                return resp["data"]["data_set_id"], "success"

            time.sleep(3)

    def train(self, dataset_id, modal_type, task_type, scene=1, primary_label="", primary_main_time_col="", id_cols=""):
        """
        模型训练
        :param dataset_id: 数据集id， 通过dataUpload获取
        :param modal_type: 模态类型。 0CSV,1VIDEO,2IMAGE,3SPEECH,4TEXT
        :param task_type: 任务类型。0二分类/分类,1多分类/检测/意图识别/匹配,2回归/定位/语音分离/序列,3时序/分隔
        :param scene: 场景标签。 枚举
        :param primary_label: 预测列
        :return: 训练项目id, 最优方案的模型id, msg
        """
        # 参数校验
        if modal_type not in [0, 1, 2, 3, 4]:
            return -1, "modal_type not support."
        if task_type not in [0, 1, 2, 3]:
            return -1, "task_type not support."

        # 创建项目
        projData = {}
        projData["modal_type"] = modal_type
        projData["name"] = "SDK_PROJ_"+str(dataset_id+time.time())

        projData["task_type"] = task_type
        # 任务描述
        projData["description"] = ""

        projData["scene"] = scene
        projData["primary_label"] = primary_label
        projData["primary_main_time_col"] = primary_main_time_col
        projData["id_cols"] = id_cols
        projData["table_relation"] = json.dumps({"primary_table": dataset_id, "secondary_tables": []})
        projData["advance_settings"] = '{"optimizer":"ga","gp_switch":"off","search_space":[{"hp_subspace":"feature_engineering","hp_values":{"KeyTimeBinSecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeBinMsecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeWeekday":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeHour":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDay":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeMonth":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeYear":{"hp_type":"bool","hp_values":[true,false]},"KeyNumDiff":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_BW_Window_1":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_FW_Window_10":{"hp_type":"bool","hp_values":[true,false]},"McCatRank":{"hp_type":"bool","hp_values":[true,false]},"McMcInnerLen":{"hp_type":"bool","hp_values":[true,false]},"GroupCntDivNunique":{"hp_type":"bool","hp_values":[true,false]},"CatCnt":{"hp_type":"bool","hp_values":[true,false]},"GroupMean":{"hp_type":"bool","hp_values":[true,false]},"GroupMax":{"hp_type":"bool","hp_values":[true,false]},"GroupMin":{"hp_type":"bool","hp_values":[true,false]},"GroupStd":{"hp_type":"bool","hp_values":[true,false]},"GroupMeanMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMaxMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMinMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"CatSegCtrOrigin":{"hp_type":"bool","hp_values":[true,false]}}},{"hp_subspace":"modeling","hp_values":{"model":{"hp_type":"choice","hp_values":[{"hp_name":"LIGHTGBM","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"RANDOMFOREST","n_estimators":{"hp_type":"cholind","hp_values":[10,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,20,2]}},{"hp_name":"GBTREE","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"n_estimators":{"hp_type":"cholind","hp_values":[2,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,10,2]}},{"hp_name":"CATBOOST","iterations":{"hp_type":"cholind","hp_values":[200,1000,10]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.01,1]},"depth":{"hp_type":"randint","hp_values":[3,10]},"l2_leaf_reg":{"hp_type":"uniform","hp_values":[0,2]}},{"hp_name":"GLM","use_glm_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"SVM","kernel":{"hp_type":"choice","hp_values":["rbf","linear","sigmoid","poly"]},"shrinking":{"hp_type":"choice","hp_values":[true,false]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]}},{"hp_name":"LINEARSVM","penalty":{"hp_type":"choice","hp_values":["l2"]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]},"multi_class":{"hp_type":"choice","hp_values":["ovr","crammer_singer"]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[10000,30000,1000]}},{"hp_name":"PASSIVEAGGRESSIVE","loss":{"hp_type":"choice","hp_values":["hinge","squared_hinge"]},"C":{"hp_type":"loguniform","hp_values":[0.001,1000]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.1,0.5]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"warm_start":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"PERCEPTRON","penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"loguniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0,0.5]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"RIDGE","solver":{"hp_type":"choice","hp_values":["auto","svd","cholesky","lsqr","sparse_cg","sag","saga"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"normalize":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"SGD","loss":{"hp_type":"choice","hp_values":["hinge","log","modified_huber","squared_hinge","perceptron"]},"penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[4000,6000,100]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.2,0.5]},"learning_rate":{"hp_type":"choice","hp_values":["optimal","constant","adaptive","invscaling"]},"eta0":{"hp_type":"uniform","hp_values":[0.001,10]}},{"hp_name":"KNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"n_neighbors":{"hp_type":"randint","hp_values":[5,30]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"RADIUSNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"radius":{"hp_type":"randint","hp_values":[800,1500]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"DECISIONTREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREES","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"n_estimators":{"hp_type":"randint","hp_values":[1,50]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,40]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"ADABOOST","base_estimator":{"hp_type":"choice","hp_values":[null]},"n_estimators":{"hp_type":"randint","hp_values":[1,100]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.001,1]}},{"hp_name":"DEEPFOREST","n_bins":{"hp_type":"randint","hp_values":[200,255]},"n_estimators":{"hp_type":"randint","hp_values":[50,100]},"bin_subsample":{"hp_type":"cholind","hp_values":[150000,250000,10000]},"max_layers":{"hp_type":"cholind","hp_values":[10,50,5]},"n_trees":{"hp_type":"cholind","hp_values":[50,200,5]},"predictor":{"hp_type":"choice","hp_values":["forest","xgboost","lightgbm"]},"n_tolerant_rounds":{"hp_type":"randint","hp_values":[2,5]},"delta":{"hp_type":"loguniform","hp_values":[1e-7,0.0001]},"partial_mode":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"XGBOOST","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"TABNET","n_d":{"hp_type":"randint","hp_values":[8,64]},"n_steps":{"hp_type":"randint","hp_values":[3,10]},"gamma":{"hp_type":"uniform","hp_values":[1,2]},"n_independent":{"hp_type":"randint","hp_values":[1,5]},"n_shared":{"hp_type":"randint","hp_values":[1,5]},"momentum":{"hp_type":"loguniform","hp_values":[0.01,0.4]}},{"hp_name":"H2O","use_h2o_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOGLUON","use_atutogluon_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOSKLEARN","use_autosklearn_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"GAUSSIANNB","var_smoothing":{"hp_type":"loguniform","hp_values":[1e-9,0.1]}},{"hp_name":"BAGGINGLINEAR","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}},{"hp_name":"BAGGINGXGBOOST","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}}]}}}],"target_train":{"train_data_ratio":80,"training_program":"指标优先","call_limit":[5,20],"instance_num":2,"call_delay":50,"gpu_num":0,"memory_limit":30,"program_num":3,"max_trials":30},"advanced_solution_1":"on","advanced_solution_2":"on","advanced_solution_3":"on"}'
        resp = self.createProj(projData)
        logging.info("createProj:%s", resp)
        if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
            return -1, -1, resp

        projId = resp["data"]["new_project_info"][0]["id"]

        # 更新高级设置
        advanceData = {}
        advanceData["project_id"] = projId
        advanceData["advance_settings"] = '{"optimizer":"ga","gp_switch":"off","search_space":[{"hp_subspace":"feature_engineering","hp_values":{"KeyTimeBinSecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeBinMsecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeWeekday":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeHour":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDay":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeMonth":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeYear":{"hp_type":"bool","hp_values":[true,false]},"KeyNumDiff":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_BW_Window_1":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_FW_Window_10":{"hp_type":"bool","hp_values":[true,false]},"McCatRank":{"hp_type":"bool","hp_values":[true,false]},"McMcInnerLen":{"hp_type":"bool","hp_values":[true,false]},"GroupCntDivNunique":{"hp_type":"bool","hp_values":[true,false]},"CatCnt":{"hp_type":"bool","hp_values":[true,false]},"GroupMean":{"hp_type":"bool","hp_values":[true,false]},"GroupMax":{"hp_type":"bool","hp_values":[true,false]},"GroupMin":{"hp_type":"bool","hp_values":[true,false]},"GroupStd":{"hp_type":"bool","hp_values":[true,false]},"GroupMeanMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMaxMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMinMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"CatSegCtrOrigin":{"hp_type":"bool","hp_values":[true,false]}}},{"hp_subspace":"modeling","hp_values":{"model":{"hp_type":"choice","hp_values":[{"hp_name":"LIGHTGBM","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"RANDOMFOREST","n_estimators":{"hp_type":"cholind","hp_values":[10,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,20,2]}},{"hp_name":"GBTREE","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"n_estimators":{"hp_type":"cholind","hp_values":[2,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,10,2]}},{"hp_name":"CATBOOST","iterations":{"hp_type":"cholind","hp_values":[200,1000,10]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.01,1]},"depth":{"hp_type":"randint","hp_values":[3,10]},"l2_leaf_reg":{"hp_type":"uniform","hp_values":[0,2]}},{"hp_name":"GLM","use_glm_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"SVM","kernel":{"hp_type":"choice","hp_values":["rbf","linear","sigmoid","poly"]},"shrinking":{"hp_type":"choice","hp_values":[true,false]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]}},{"hp_name":"LINEARSVM","penalty":{"hp_type":"choice","hp_values":["l2"]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]},"multi_class":{"hp_type":"choice","hp_values":["ovr","crammer_singer"]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[10000,30000,1000]}},{"hp_name":"PASSIVEAGGRESSIVE","loss":{"hp_type":"choice","hp_values":["hinge","squared_hinge"]},"C":{"hp_type":"loguniform","hp_values":[0.001,1000]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.1,0.5]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"warm_start":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"PERCEPTRON","penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"loguniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0,0.5]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"RIDGE","solver":{"hp_type":"choice","hp_values":["auto","svd","cholesky","lsqr","sparse_cg","sag","saga"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"normalize":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"SGD","loss":{"hp_type":"choice","hp_values":["hinge","log","modified_huber","squared_hinge","perceptron"]},"penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[4000,6000,100]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.2,0.5]},"learning_rate":{"hp_type":"choice","hp_values":["optimal","constant","adaptive","invscaling"]},"eta0":{"hp_type":"uniform","hp_values":[0.001,10]}},{"hp_name":"KNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"n_neighbors":{"hp_type":"randint","hp_values":[5,30]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"RADIUSNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"radius":{"hp_type":"randint","hp_values":[800,1500]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"DECISIONTREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREES","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"n_estimators":{"hp_type":"randint","hp_values":[1,50]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,40]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"ADABOOST","base_estimator":{"hp_type":"choice","hp_values":[null]},"n_estimators":{"hp_type":"randint","hp_values":[1,100]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.001,1]}},{"hp_name":"DEEPFOREST","n_bins":{"hp_type":"randint","hp_values":[200,255]},"n_estimators":{"hp_type":"randint","hp_values":[50,100]},"bin_subsample":{"hp_type":"cholind","hp_values":[150000,250000,10000]},"max_layers":{"hp_type":"cholind","hp_values":[10,50,5]},"n_trees":{"hp_type":"cholind","hp_values":[50,200,5]},"predictor":{"hp_type":"choice","hp_values":["forest","xgboost","lightgbm"]},"n_tolerant_rounds":{"hp_type":"randint","hp_values":[2,5]},"delta":{"hp_type":"loguniform","hp_values":[1e-7,0.0001]},"partial_mode":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"XGBOOST","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"TABNET","n_d":{"hp_type":"randint","hp_values":[8,64]},"n_steps":{"hp_type":"randint","hp_values":[3,10]},"gamma":{"hp_type":"uniform","hp_values":[1,2]},"n_independent":{"hp_type":"randint","hp_values":[1,5]},"n_shared":{"hp_type":"randint","hp_values":[1,5]},"momentum":{"hp_type":"loguniform","hp_values":[0.01,0.4]}},{"hp_name":"H2O","use_h2o_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOGLUON","use_atutogluon_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOSKLEARN","use_autosklearn_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"GAUSSIANNB","var_smoothing":{"hp_type":"loguniform","hp_values":[1e-9,0.1]}},{"hp_name":"BAGGINGLINEAR","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}},{"hp_name":"BAGGINGXGBOOST","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}}]}}}],"target_train":{"train_data_ratio":80,"training_program":"指标优先","call_limit":[5,20],"instance_num":2,"call_delay":50,"gpu_num":0,"memory_limit":30,"program_num":3,"max_trials":3},"advanced_solution_1":"on","advanced_solution_2":"on","advanced_solution_3":"on"}'

        resp = self.projAdvanceSetting(advanceData)
        if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
            return -1, -1, resp

        # 开始训练
        trainData = {}
        trainData["project_id"] = projId
        resp = self.projTrain(trainData)

        # 轮询查询训练进度, 5s一次
        while True:
            projInfodata = {}

            projInfodata["project_id"] = projId
            resp = self.projInfo(projInfodata)
            logging.info(resp)

            if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
                return -1, -1, resp
            # 训练成功
            if resp["data"]["status"] == 2:
                break

            # 训练失败
            if resp["data"]["status"] == 3:
                return -1, -1, "oho, train fail."

            time.sleep(5)

        # 获取最终方案
        trainResultData = {}

        trainResultData["project_id"] = projId
        resp = self.projTrainResult(trainResultData)
        logging.info("projTrainResult:%s", resp)
        if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
            return -1, -1, resp
        if len(resp["data"]["scheme"]) < 1:
            return -1, -1, resp

        trial_no = resp["data"]["scheme"][0]["trial_no"]

        # 获取最佳方案的模型id
        trainModeData = {}

        trainModeData["project_id"] = projId
        trainModeData["trial_no"] = trial_no
        resp = self.trainModeInfo(trainModeData)
        logging.info(resp)
        if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
            return -1, -1, resp

        model_id = resp["data"][0]["model_id"]

        return projId, model_id, "success"

    def deploy(self, proj_id, model_id):
        """
        推理服务部署
        :param proj_id: 训练项目id。 通过train获取
        :param model_id: 最优方案的模型id。 通过train获取
        :return: 服务id, msg
        """
        # 创建推理服务
        inferSvrData = {}

        svrName = "infer-svr-" + str(proj_id) + "-" + str(model_id)
        inferSvrData["project_id"] = proj_id
        inferSvrData["model_inst_id"] = model_id
        inferSvrData["name"] = svrName
        inferSvrData["used_model"] = "default"
        resp = self.inferSvr(inferSvrData)
        logging.info("inferSvr:%s", resp)
        if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
            return -1, resp

        # 判断推理启动完成, 待优化
        svr_id = -1
        while True:
            resp = self.getSvrList()
            if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
                return -1, resp
            for svr in resp["data"]:
                if svr["service_name"] == svrName:
                    if svr["status"] == 2:
                        svr_id = svr["id"]
                        break

            if svr_id > 0:
                break

            time.sleep(3)

        return svr_id, "success"











