import json
import time
import logging

import six
import trafaret as t
import deepwisdom.errors as err

from deepwisdom._compat import Int, String

from .api_object import APIObject
from deepwisdom.enums import API_URL


class Model(APIObject):
    """

    """


class DicTableModel(Model):
    """
    表格二分类
    """


class ModelInstance(APIObject):
    """

    """
    _converter = t.Dict(
        {
            t.Key("model_id"): Int,
            t.Key("model_name"): String,
        }
    ).allow_extra("*")

    def __init__(
            self,
            project_id,
            trial_no,
            trial_type,
            model_id,
            model_name=None
    ):
        self.project_id = project_id
        self.trial_no = trial_no
        self.trial_type = trial_type
        self.model_id = model_id
        self.model_name = model_name
