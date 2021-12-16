import json
import time
import logging

import six
import trafaret as t
import deepwisdom.errors as err

from deepwisdom._compat import Int, String

from .api_object import APIObject
from deepwisdom.enums import API_URL


class Solution(APIObject):
    """

    """
    _converter = t.Dict(
        {
            t.Key("trial_no"): Int,
            t.Key("trial_type"): Int,
            t.Key("model_name", optional=True): String
        }
    ).allow_extra("*")

    def __init__(
            self,
            project_id,
            trial_no,
            trial_type,
            model_name=None
    ):
        """
        方案类
        Args:
            project_id (int):
            trial_no (int):
            trial_type (int):
            model_name (str):
        """
        self.project_id = project_id
        self.trial_no = trial_no
        self.trial_type = trial_type
        self.model_name = model_name

    def get_detail(self, tab_type=1):
        """
        这里直接返回详情json, 后续梳理返回结构可细化
        Args:
            tab_type (int):

        Returns:

        """
        data = {
            "project_id": self.project_id,
            "trial_no": self.trial_no,
            "tab_type": tab_type
        }

        return self._server_data(API_URL.PROJECT_MODEL, data)


