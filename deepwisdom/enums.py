def enum(*vals, **enums):
    """
    Enum without third party libs and compatible with py2 and py3 versions.
    """
    enums.update(dict(zip(vals, vals)))
    return type("Enum", (), enums)


DEFAULT_DOMAIN = ""

# This is deprecated, to be removed in 3.0.
MODEL_JOB_STATUS = enum(ERROR="error", INPROGRESS="inprogress", QUEUE="queue")

# default time out values in seconds for waiting response from client
DEFAULT_TIMEOUT = enum(
    CONNECT=6.05,  # time in seconds for the connection to server to be established
    SOCKET=60,
    READ=60,  # time in seconds after which to conclude the server isn't responding anymore
    UPLOAD=600,  # time in seconds after which to conclude that project dataset cannot be uploaded
)

API_DOMAIN = enum(
    ACCESS_TOKEN="",
    API=""
)

API_URL = enum(
    AUTH="http://192.168.50.121:31905/sdk/appmng/token",
    DATASET_PREPARE="sdk/sdksvr/datasetprepare",
    FILE_UPLOAD="sdk/sdksvr/fileupload",
    DATASET_UPLOAD="sdk/sdksvr/datasetupload",
    DATASET_QUERY="http://192.168.50.24:30161/sdk/sdksvr/querydataset",
    DATASET_INFO="sdk/sdksvr/datasetinfo",
    PROJECT_CREATE="sdk/sdksvr/createproj",
    PROJECT_TRAIN="sdk/sdksvr/projtrain",
    PROJECT_RETRAIN="sdk/sdksvr/projretrain",
    PROJECT_INFO="sdk/sdksvr/projinfo",
    PROJECT_TRAIN_RESULT="/sdk/sdksvr/trainresult",

    PREDICTION_DETAIL="sdk/sdksvr/projeval/detail",
    PREDICTION_PREDICT="sdk/sdksvr/projeval/predict",
    PREDICTION_LIST="sdk/sdksvr/projeval/list",
    PREDICTION_DELETE="sdk/sdksvr/projeval/delete",
    PREDICTION_DATASET_DOWNLOAD="sdk/sdksvr/projeval/dataset_download",
    PREDICTION_RESULT_DOWNLOAD="sdk/sdksvr/projeval/result_download",

    DEPLOY_CREATE_SERVICE='sdk/sdksvr/deploy/create',
    DEPLOY_GET_SERVICE_DETAIL='sdk/sdksvr/deploy/detail',
    DEPLOY_LIST_DEPLOYMENTS='sdk/sdksvr/deploy/list',
    DEPLOY_RESIDENT_DEPLOYMENT='sdk/sdksvr/deploy/resident',  # 推理服务常驻
    DEPLOY_RENAME_DEPLOYMENT='sdk/sdksvr/deploy/rename',
    DEPLOY_DELETE_DEPLOYMENT='sdk/sdksvr/deploy/delete',
    DEPLOY_GET_DEPLOYMENT_LOG='sdk/sdksvr/deploy/logs',

    DATASET_DOWNLOAD_HOST="http://192.168.50.24:5000/proxy/static/"

)


class _DEPLOYMENT_HEALTH_STATUS(object):
    PASSING = "passing"
    WARNING = "warning"
    FAILING = "failing"
    UNKNOWN = "unknown"

    ALL = [PASSING, WARNING, FAILING, UNKNOWN]


class DEPLOYMENT_SERVICE_HEALTH_STATUS(_DEPLOYMENT_HEALTH_STATUS):
    pass


class DEPLOYMENT_MODEL_HEALTH_STATUS(_DEPLOYMENT_HEALTH_STATUS):
    pass
