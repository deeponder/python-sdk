import logging

from dw_tj import DwTj
import os

import json

# 1. 数据上传
def datasetPrepareTest():
    data = {}

    data["modal_type"] = 0
    data["filename"] = "dataset_upload_test.csv"
    data["upload_id"] = upload_id

    resp = client.datasetPrepare(data)
    print(resp)

def fileUploadTest():
    data = {}

    data["upload_id"] = upload_id
    data["chunk_id"] = upload_id
    files = {
        "file": (os.path.basename(filepath), open(filepath, 'rb'), 'application/octet-stream')
    }
    resp = client.fileUpload(files, data)
    print(resp)

"""
upload_id: zhipeng_test_data.csv-2021-8-17 19:42:59-2f1e861d563b5782f9dcd23ac8b98a38
filename: zhipeng_test_data.csv
chunk_id_list: ["zhipeng_test_data.csv-2021-8-17 19:42:59-2f1e861d563b5782f9dcd23ac8b98a38-0"]
modal_type: 0
sep: \t
annotation_type: 1
desc: 0
dataset_scene_id: 1
resp: {"code": 200, "message": "ok", "data": {"ret": 1}}
"""
def datasetUploadTest():
    data = {}

    data["filename"] = "dataset_upload_test.csv"
    data["upload_id"] = upload_id
    data["chunk_id_list"] = json.dumps([upload_id])
    data["modal_type"] = 0
    data["seq"] = "\\t"
    data["annotation_type"] = 1
    # 场景Id， 二分等
    data["dataset_scene_id"] = 1

    resp = client.datasetUpload(data)
    print(resp)

# 2. 创建项目, 回包project_id
def creatProjTest():
    data = {}
    # 模态：  0表格,1视频,2图片,3音频,4文本
    data["modal_type"] = 0
    data["name"] = "zhipeng-test6"
    # 任务类型 0二分类/分类,1多分类/检测/意图识别/匹配,2回归/定位/语音分离/序列,3时序/分隔
    data["task_type"] = 0
    # 任务描述
    data["description"] = "xxx"
    #
    data["scene"] = 221
    data["primary_label"] = "is_marry"
    data["primary_main_time_col"] = ""
    data["table_relation"] = '{"primary_table": 3719,"secondary_tables":[]}'
    data["advance_settings"] = '{"optimizer":"ga","gp_switch":"off","search_space":[{"hp_subspace":"feature_engineering","hp_values":{"KeyTimeBinSecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeBinMsecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeWeekday":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeHour":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDay":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeMonth":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeYear":{"hp_type":"bool","hp_values":[true,false]},"KeyNumDiff":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_BW_Window_1":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_FW_Window_10":{"hp_type":"bool","hp_values":[true,false]},"McCatRank":{"hp_type":"bool","hp_values":[true,false]},"McMcInnerLen":{"hp_type":"bool","hp_values":[true,false]},"GroupCntDivNunique":{"hp_type":"bool","hp_values":[true,false]},"CatCnt":{"hp_type":"bool","hp_values":[true,false]},"GroupMean":{"hp_type":"bool","hp_values":[true,false]},"GroupMax":{"hp_type":"bool","hp_values":[true,false]},"GroupMin":{"hp_type":"bool","hp_values":[true,false]},"GroupStd":{"hp_type":"bool","hp_values":[true,false]},"GroupMeanMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMaxMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMinMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"CatSegCtrOrigin":{"hp_type":"bool","hp_values":[true,false]}}},{"hp_subspace":"modeling","hp_values":{"model":{"hp_type":"choice","hp_values":[{"hp_name":"LIGHTGBM","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"RANDOMFOREST","n_estimators":{"hp_type":"cholind","hp_values":[10,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,20,2]}},{"hp_name":"GBTREE","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"n_estimators":{"hp_type":"cholind","hp_values":[2,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,10,2]}},{"hp_name":"CATBOOST","iterations":{"hp_type":"cholind","hp_values":[200,1000,10]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.01,1]},"depth":{"hp_type":"randint","hp_values":[3,10]},"l2_leaf_reg":{"hp_type":"uniform","hp_values":[0,2]}},{"hp_name":"GLM","use_glm_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"SVM","kernel":{"hp_type":"choice","hp_values":["rbf","linear","sigmoid","poly"]},"shrinking":{"hp_type":"choice","hp_values":[true,false]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]}},{"hp_name":"LINEARSVM","penalty":{"hp_type":"choice","hp_values":["l2"]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]},"multi_class":{"hp_type":"choice","hp_values":["ovr","crammer_singer"]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[10000,30000,1000]}},{"hp_name":"PASSIVEAGGRESSIVE","loss":{"hp_type":"choice","hp_values":["hinge","squared_hinge"]},"C":{"hp_type":"loguniform","hp_values":[0.001,1000]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.1,0.5]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"warm_start":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"PERCEPTRON","penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"loguniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0,0.5]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"RIDGE","solver":{"hp_type":"choice","hp_values":["auto","svd","cholesky","lsqr","sparse_cg","sag","saga"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"normalize":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"SGD","loss":{"hp_type":"choice","hp_values":["hinge","log","modified_huber","squared_hinge","perceptron"]},"penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[4000,6000,100]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.2,0.5]},"learning_rate":{"hp_type":"choice","hp_values":["optimal","constant","adaptive","invscaling"]},"eta0":{"hp_type":"uniform","hp_values":[0.001,10]}},{"hp_name":"KNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"n_neighbors":{"hp_type":"randint","hp_values":[5,30]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"RADIUSNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"radius":{"hp_type":"randint","hp_values":[800,1500]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"DECISIONTREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREES","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"n_estimators":{"hp_type":"randint","hp_values":[1,50]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,40]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"ADABOOST","base_estimator":{"hp_type":"choice","hp_values":[null]},"n_estimators":{"hp_type":"randint","hp_values":[1,100]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.001,1]}},{"hp_name":"DEEPFOREST","n_bins":{"hp_type":"randint","hp_values":[200,255]},"n_estimators":{"hp_type":"randint","hp_values":[50,100]},"bin_subsample":{"hp_type":"cholind","hp_values":[150000,250000,10000]},"max_layers":{"hp_type":"cholind","hp_values":[10,50,5]},"n_trees":{"hp_type":"cholind","hp_values":[50,200,5]},"predictor":{"hp_type":"choice","hp_values":["forest","xgboost","lightgbm"]},"n_tolerant_rounds":{"hp_type":"randint","hp_values":[2,5]},"delta":{"hp_type":"loguniform","hp_values":[1e-7,0.0001]},"partial_mode":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"XGBOOST","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"TABNET","n_d":{"hp_type":"randint","hp_values":[8,64]},"n_steps":{"hp_type":"randint","hp_values":[3,10]},"gamma":{"hp_type":"uniform","hp_values":[1,2]},"n_independent":{"hp_type":"randint","hp_values":[1,5]},"n_shared":{"hp_type":"randint","hp_values":[1,5]},"momentum":{"hp_type":"loguniform","hp_values":[0.01,0.4]}},{"hp_name":"H2O","use_h2o_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOGLUON","use_atutogluon_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOSKLEARN","use_autosklearn_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"GAUSSIANNB","var_smoothing":{"hp_type":"loguniform","hp_values":[1e-9,0.1]}},{"hp_name":"BAGGINGLINEAR","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}},{"hp_name":"BAGGINGXGBOOST","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}}]}}}],"target_train":{"train_data_ratio":80,"training_program":"指标优先","call_limit":[5,20],"instance_num":2,"call_delay":50,"gpu_num":0,"memory_limit":30,"program_num":3,"max_trials":30},"advanced_solution_1":"on","advanced_solution_2":"on","advanced_solution_3":"on"}'
    resp = client.createProj(data)
    print(resp)

# 需要屏蔽掉
def projAdvanceSetting():
    data = {}
    data["project_id"] = 2593
    data["advance_settings"] = '{"optimizer":"ga","gp_switch":"off","search_space":[{"hp_subspace":"feature_engineering","hp_values":{"KeyTimeBinSecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeBinMsecond":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeWeekday":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeHour":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDay":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeMonth":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeYear":{"hp_type":"bool","hp_values":[true,false]},"KeyNumDiff":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_BW_Window_1":{"hp_type":"bool","hp_values":[true,false]},"KeyTimeDiff_FW_Window_10":{"hp_type":"bool","hp_values":[true,false]},"McCatRank":{"hp_type":"bool","hp_values":[true,false]},"McMcInnerLen":{"hp_type":"bool","hp_values":[true,false]},"GroupCntDivNunique":{"hp_type":"bool","hp_values":[true,false]},"CatCnt":{"hp_type":"bool","hp_values":[true,false]},"GroupMean":{"hp_type":"bool","hp_values":[true,false]},"GroupMax":{"hp_type":"bool","hp_values":[true,false]},"GroupMin":{"hp_type":"bool","hp_values":[true,false]},"GroupStd":{"hp_type":"bool","hp_values":[true,false]},"GroupMeanMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMaxMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"GroupMinMinusSelf":{"hp_type":"bool","hp_values":[true,false]},"CatSegCtrOrigin":{"hp_type":"bool","hp_values":[true,false]}}},{"hp_subspace":"modeling","hp_values":{"model":{"hp_type":"choice","hp_values":[{"hp_name":"LIGHTGBM","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"RANDOMFOREST","n_estimators":{"hp_type":"cholind","hp_values":[10,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,20,2]}},{"hp_name":"GBTREE","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"n_estimators":{"hp_type":"cholind","hp_values":[2,200,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"min_samples_leaf":{"hp_type":"cholind","hp_values":[2,100,2]},"min_samples_split":{"hp_type":"cholind","hp_values":[2,10,2]}},{"hp_name":"CATBOOST","iterations":{"hp_type":"cholind","hp_values":[200,1000,10]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.01,1]},"depth":{"hp_type":"randint","hp_values":[3,10]},"l2_leaf_reg":{"hp_type":"uniform","hp_values":[0,2]}},{"hp_name":"GLM","use_glm_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"SVM","kernel":{"hp_type":"choice","hp_values":["rbf","linear","sigmoid","poly"]},"shrinking":{"hp_type":"choice","hp_values":[true,false]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]}},{"hp_name":"LINEARSVM","penalty":{"hp_type":"choice","hp_values":["l2"]},"C":{"hp_type":"uniform","hp_values":[0.001,1000]},"multi_class":{"hp_type":"choice","hp_values":["ovr","crammer_singer"]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[10000,30000,1000]}},{"hp_name":"PASSIVEAGGRESSIVE","loss":{"hp_type":"choice","hp_values":["hinge","squared_hinge"]},"C":{"hp_type":"loguniform","hp_values":[0.001,1000]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.1,0.5]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"warm_start":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"PERCEPTRON","penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"loguniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0,0.5]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"RIDGE","solver":{"hp_type":"choice","hp_values":["auto","svd","cholesky","lsqr","sparse_cg","sag","saga"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"normalize":{"hp_type":"choice","hp_values":[true,false]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]}},{"hp_name":"SGD","loss":{"hp_type":"choice","hp_values":["hinge","log","modified_huber","squared_hinge","perceptron"]},"penalty":{"hp_type":"choice","hp_values":["l1","l2","elasticnet"]},"alpha":{"hp_type":"uniform","hp_values":[0.0001,1000]},"fit_intercept":{"hp_type":"choice","hp_values":[true,false]},"shuffle":{"hp_type":"choice","hp_values":[true,false]},"max_iter":{"hp_type":"cholind","hp_values":[4000,6000,100]},"tol":{"hp_type":"loguniform","hp_values":[0.00001,1]},"early_stopping":{"hp_type":"choice","hp_values":[true,false]},"validation_fraction":{"hp_type":"uniform","hp_values":[0.2,0.5]},"learning_rate":{"hp_type":"choice","hp_values":["optimal","constant","adaptive","invscaling"]},"eta0":{"hp_type":"uniform","hp_values":[0.001,10]}},{"hp_name":"KNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"n_neighbors":{"hp_type":"randint","hp_values":[5,30]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"RADIUSNEIGHBORS","algorithm":{"hp_type":"choice","hp_values":["auto","ball_tree","kd_tree","brute"]},"radius":{"hp_type":"randint","hp_values":[800,1500]},"weights":{"hp_type":"choice","hp_values":["uniform","distance"]},"leaf_size":{"hp_type":"randint","hp_values":[10,50]},"p":{"hp_type":"choice","hp_values":[1,2]},"metric":{"hp_type":"choice","hp_values":["euclidean","manhattan","chebyshev","minkowski"]}},{"hp_name":"DECISIONTREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREE","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"splitter":{"hp_type":"choice","hp_values":["best","random"]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,20]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"EXTRATREES","criterion":{"hp_type":"choice","hp_values":["gini","entropy"]},"n_estimators":{"hp_type":"randint","hp_values":[1,50]},"min_samples_leaf":{"hp_type":"randint","hp_values":[2,10]},"min_samples_split":{"hp_type":"randint","hp_values":[2,10]},"max_depth":{"hp_type":"cholind","hp_values":[10,100,5]},"max_features":{"hp_type":"choice","hp_values":["log2","auto","sqrt",null]},"max_leaf_nodes":{"hp_type":"randint","hp_values":[5,40]},"min_impurity_decrease":{"hp_type":"uniform","hp_values":[0,5]}},{"hp_name":"ADABOOST","base_estimator":{"hp_type":"choice","hp_values":[null]},"n_estimators":{"hp_type":"randint","hp_values":[1,100]},"learning_rate":{"hp_type":"loguniform","hp_values":[0.001,1]}},{"hp_name":"DEEPFOREST","n_bins":{"hp_type":"randint","hp_values":[200,255]},"n_estimators":{"hp_type":"randint","hp_values":[50,100]},"bin_subsample":{"hp_type":"cholind","hp_values":[150000,250000,10000]},"max_layers":{"hp_type":"cholind","hp_values":[10,50,5]},"n_trees":{"hp_type":"cholind","hp_values":[50,200,5]},"predictor":{"hp_type":"choice","hp_values":["forest","xgboost","lightgbm"]},"n_tolerant_rounds":{"hp_type":"randint","hp_values":[2,5]},"delta":{"hp_type":"loguniform","hp_values":[1e-7,0.0001]},"partial_mode":{"hp_type":"choice","hp_values":[true,false]}},{"hp_name":"XGBOOST","learning_rate":{"hp_type":"loguniform","hp_values":[0.01,2]},"max_depth":{"hp_type":"randint","hp_values":[3,10]},"num_leaves":{"hp_type":"cholind","hp_values":[10,200,5]},"feature_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_fraction":{"hp_type":"quniform","hp_values":[0.5,1,0.1]},"bagging_freq":{"hp_type":"cholind","hp_values":[0,50,3]},"reg_alpha":{"hp_type":"uniform","hp_values":[0,2]},"reg_lambda":{"hp_type":"uniform","hp_values":[0,2]},"min_child_weight":{"hp_type":"uniform","hp_values":[0.5,10]},"min_sum_hessian_in_leaf":{"hp_type":"uniform","hp_values":[0,1]},"min_data_in_leaf":{"hp_type":"cholind","hp_values":[21,60,3]}},{"hp_name":"TABNET","n_d":{"hp_type":"randint","hp_values":[8,64]},"n_steps":{"hp_type":"randint","hp_values":[3,10]},"gamma":{"hp_type":"uniform","hp_values":[1,2]},"n_independent":{"hp_type":"randint","hp_values":[1,5]},"n_shared":{"hp_type":"randint","hp_values":[1,5]},"momentum":{"hp_type":"loguniform","hp_values":[0.01,0.4]}},{"hp_name":"H2O","use_h2o_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOGLUON","use_atutogluon_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"AUTOSKLEARN","use_autosklearn_constant":{"hp_type":"choice","hp_values":[1]}},{"hp_name":"GAUSSIANNB","var_smoothing":{"hp_type":"loguniform","hp_values":[1e-9,0.1]}},{"hp_name":"BAGGINGLINEAR","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}},{"hp_name":"BAGGINGXGBOOST","n_estimators":{"hp_type":"cholind","hp_values":[100,300,10]},"max_samples":{"hp_type":"randint","hp_values":[1,5]},"max_features":{"hp_type":"randint","hp_values":[1,5]}}]}}}],"target_train":{"train_data_ratio":80,"training_program":"指标优先","call_limit":[5,20],"instance_num":2,"call_delay":50,"gpu_num":0,"memory_limit":30,"program_num":3,"max_trials":30},"advanced_solution_1":"on","advanced_solution_2":"on","advanced_solution_3":"on"}'

    resp = client.projAdvanceSetting(data)
    print(resp)


# 3. 项目训练
# 开始训练
def trainTest():
    data = {}

    data["project_id"] = 2593
    resp = client.projTrain(data)
    print(resp)
# 重新训练
def retrainTest():
    data = {}

    data["project_id"] = 2593
    resp = client.projReTrain(data)
    print(resp)

# 4 查看训练进度  status=2 为成功
"""
{
    "code":200,
    "message":"ok",
    "data":{
        "id":2586,
        "parent_project_id":null,
        "user_id":47,
        "name":"zhipeng-test5",
        "modal_type":0,
        "task_type":0,
        "template":0,
        "description":"xxx",
        "scene":221,
        "model_path":null,
        "train_task_id":"cca4f3f4-d90e-477c-9ae1-738340743768",
        "status":1,
        "collect_type":0,
        "infer_task_id":null,
        "infer_status":0,
        "eval_data":null,
        "table_relation":"{\\"primary_table\\": 3719, \\"secondary_tables\\": []}",
        "primary_label":"is_marry",
        "primary_main_time_col":"",
        "pri_sec_relation":"[]",
        "advance_settings":"",
        "update_type":null,
        "test_samples":null,
        "infer_uri":null,
        "proj_version":"v4.0",
        "is_del":0,
        "create_time":"2021-08-16 19:27:07",
        "update_time":"2021-08-16 19:29:43",
        "latest_run_time":null,
        "service_id":null
    }
}
"""
def projInfoTest():
    data = {}

    data["project_id"] = 2593
    resp = client.projInfo(data)
    print(resp)

# 5. 获取训练结果/最终方案
"""
{
    "code":200,
    "message":"ok",
    "data":{
        "scheme":[
            {
                "param_space":Object{...},
                "feature_importance":Object{...},
                "model_version":1629120430,
                "model_name":"AUTOGLUON",
                "trial_no":29
            },
            Object{...},
            Object{...},
            Object{...},
            Object{...},
            Object{...}
        ]
    }
}
"""
def trainResultTest():
    data = {}

    data["project_id"] = 2593
    resp = client.projTrainResult(data)
    print(json.dumps(resp, indent=1))


# 获取方案对应的模型信息(id等)  368
"""
{
 "code": 200,
 "message": "ok",
 "data": [
  {
   "model_id": 3685,
   "model_name": "AUTOGLUON_trial_0b249948"
  }
 ]
}
"""
def trainModelInfo():
    data = {}

    data["project_id"] = 2593
    data["trial_no"] = 29
    resp = client.trainModeInfo(data)
    print(json.dumps(resp, indent=1))

"""
1. 项目id，project_id 
2. 模型id, model_inst_id
"""

# 6. 离线验证 二期
#dataset_id需要通过/predict/datasets获取
def projEvalTest():
    data = {}

    data["model_inst_id"] = 3694
    data["dataset_id"] = 3724
    resp = client.projEval(data)
    print(json.dumps(resp, indent=1))

# 7. 新建推理服务 & 获取服务列表
def inferSvrTest():
    data = {}

    data["project_id"] = 2593
    data["model_inst_id"] = 3694
    data["name"] = "zhipeng-test-svr3"
    data["used_model"] = "default"
    resp = client.inferSvr(data)
    print(json.dumps(resp, indent=1))

"""
{
 "code": 200,
 "message": "ok",
 "pages": 1,
 "count": 1,
 "data": [
  {
   "id": 134,
   "project_id": 2587,
   "service_name": "zhipeng-test-svr1",
   "create_time": "2021-08-17 14:19:45",
   "project_name": "0816-zhipeng_test_data",
   "deploy_model": "AUTOGLUON_trial_0b249948",
   "status": 2,
   "model_effect": 0.5538
  }
 ]
}
"""
# status = 2为成功
def getSvrListTest():
    resp = client.getSvrList()
    print(json.dumps(resp, indent=1))


# # 8. 启停推理服务
def svrOptTest():
    data = {}

    # svc_id需要从服务列表获取
    data["svc_id"] = 135
    # 0停止， 1启动
    data["op"] = 1
    resp = client.svrOpt(data)
    print(json.dumps(resp, indent=1))


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    # 创建sdk客户端
    client = DwTj(4, "RrTLKoGrgKRXkSJAstcndNLa", "xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7", "http://sdksvr.autotable.172.16.0.15.nip.io:31746", "http://appmng.autotable.172.16.0.15.nip.io:31746")

    # 上传数据集， 存储数据集id
    filepath = os.path.join(os.path.expandvars('$HOME'), "Downloads", "data_upload_test.csv")
    upload_id = client.getUploadId(filepath)
    datasetid, msg = client.dataUpload("/Users/up/Downloads/data_upload_test.csv", 0)
    if datasetid < 0:
        print("dataset upload fail", msg)
        exit(0)
    print(datasetid, msg)


    # 开始训练， 存储最优方案
    projId, model_id, msg = client.train(datasetid, 0, 0, 221, "is_marry")
    if projId < 0 or model_id < 0:
        print("tain fail", msg)
        exit(0)
    print(projId, model_id, msg)

    # 部署最优方案服务， 提供api接口调用
    svc_id, msg = client.deploy(projId, model_id)
    print("svc_id", svc_id)

