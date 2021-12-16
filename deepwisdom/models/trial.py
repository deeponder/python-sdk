import json
import time
import logging

import six
import trafaret as t
import deepwisdom.errors as err

from deepwisdom._compat import Int, String

from .api_object import APIObject
from deepwisdom.enums import API_URL
from typing import Optional, List


_effect_metric_converter = t.Dict(
    {
        t.Key("AUC", optional=True) >> "auc": t.Float,
        t.Key("F1-score", optional=True) >> "f1_score": t.Float,
        t.Key("MacroF1", optional=True) >> "macro_f1": t.Float,
        t.Key("MicroF1", optional=True) >> "micro_f1": t.Float,
        t.Key("WeightF1", optional=True) >> "weight_f1": t.Float,
        t.Key("KS", optional=True) >> "ks": t.Float,
        t.Key("LogLoss", optional=True) >> "log_loss": t.Float,
        t.Key("ACC", optional=True) >> "acc": t.Float,
        t.Key("Precision", optional=True) >> "precision": t.Float,
        t.Key("EER", optional=True) >> "eer": t.Float,
        t.Key("MCC", optional=True) >> "mcc": t.Float,
    }
).ignore_extra("*")
class EffectMetric(APIObject):
    """

    """
    def __init__(
            self,
            auc=None,
            f1_score=None,
            macro_f1=None,
            micro_f1=None,
            weight_f1=None,
            mcc=None,
            ks=None,
            log_loss=None,
            acc=None,
            precision=None,
            eer=None
    ):
        self.auc = auc
        self.f1_score = f1_score
        self.macro_f1 = macro_f1
        self.micro_f1 = micro_f1
        self.weight_f1 = weight_f1
        self.mcc = mcc
        self.ks = ks
        self.log_loss = log_loss
        self.acc = acc
        self.precision = precision
        self.eer = eer


_performance_metric_converter = t.Dict(
    {
        t.Key("FPS", optional=True) >> "fps": t.Float,
        t.Key("ICT", optional=True) >> "ict": t.Float,
        t.Key("FLOPs", optional=True) >> "flops": t.Int,
        t.Key("MaxMem", optional=True) >> "max_mem": t.Float

    }
).ignore_extra("*")
class PerformanceMetric(APIObject):
    """

    """
    _converter = _performance_metric_converter

    def __init__(
            self,
            fps=None,
            ict=None,
            flops=None,
            max_mem=None
    ):
        self.fps = fps
        self.ict = ict
        self.flops = flops
        self.max_mem = max_mem


_metric_converter = t.Dict(
    {
        t.Key("effect_metrics", optional=True): _effect_metric_converter,
        t.Key("performance_metrics", optional=True): _performance_metric_converter
    }
).ignore_extra("*")
class Metric(APIObject):
    """

    """
    _converter = _metric_converter

    def __init__(
            self,
            performance_metrics=None,
            effect_metrics=None
    ):
        self.performance_metrics = PerformanceMetric(**performance_metrics)
        self.effect_metrics = EffectMetric(**effect_metrics)

class Trial(APIObject):
    """

    """
    _converter = t.Dict(
        {
            t.Key("trial_no"): Int,
            t.Key("trial_type"): Int,
            t.Key("model_name", optional=True): String,
            t.Key("status"): Int,
            t.Key("best_metric_key"): String,
            t.Key("best_metric_value"): t.Float,
            t.Key("time_consuming"): t.Float,
            t.Key("start_time", optional=True): t.Float,
            t.Key("end_time", optional=True): t.Float,
            t.Key("is_model", optional=True): Int,
            t.Key("trial_metric", optional=True): _metric_converter
        }
    ).allow_extra("*")

    def __init__(
            self,
            trial_no,
            trial_type=None,
            status=None,
            best_metric_key=None,
            best_metric_value=None,
            time_consuming=None,
            start_time=None,
            end_time=None,
            is_model=None,
            trial_metric=None
    ):
        self.trial_no = trial_no
        self.trial_type = trial_type
        self.status = status,
        self.best_metric_key = best_metric_key
        self.best_metric_value = best_metric_value
        self.time_consuming = time_consuming
        self.start_time = start_time
        self.end_time = end_time
        self.is_model = is_model
        self.trial_metric = Metric(**trial_metric)








