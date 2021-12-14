import json
import time

import six
import trafaret as t
import deepwisdom.errors as err

from deepwisdom._compat import Int, String

from .api_object import APIObject
from deepwisdom.enums import API_URL


class Project(APIObject):
    """

    """
    _converter = t.Dict(
        {
            t.Key("id", optional=True) >> "id": String(allow_blank=True),
            t.Key("name"): String,
            t.Key("user_id"): Int,
            t.Key("model_type") >> "modal_type": Int,
            t.Key("task_type"): Int,
            t.Key("description"): String,
            t.Key("status"): Int,

        }
    ).allow_extra("*")

    def __init__(
            self,
            id,
            name=None,
            user_id=None,
            model_type=None,
            task_type=None,
            description=None,
            status=None,
    ):
        self.id = id,
        self.name = name,
        self.user_id = user_id,
        self.model_type = model_type,
        self.task_type = task_type,
        self.description = description,
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
            advance_settings=None,
    ):
        """
        :param dataset_id:
        :param name:
        :param model_type:
        :param task_type:
        :param description:
        :param scene:
        :param primary_label:
        :param primary_main_time_col:
        :param id_cols:
        :param table_relation:
        :param advance_settings:
        :return:
        """
        projData = {}
        projData["modal_type"] = model_type
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
        resp = cls._client._post(API_URL.PROJECT_CREATE, projData)
        if resp["code"] != 200 or "data" in resp and "ret" in resp["data"] and resp["data"]["ret"] != 1:
            return -1, resp

        projId = resp["data"]["new_project_info"][0]["id"]


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
        self.pri_dataset_id=pri_dataset_id,
        self.sec_dataset_id=sec_dataset_id,
        self.main_col=main_col,
        self.main_col_type=main_col_type,
        self.relation_col=relation_col,
        self.relation_col_type=relation_col_type

