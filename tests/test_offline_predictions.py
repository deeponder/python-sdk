import json
from unittest import TestCase
from deepwisdom.models.offline_predictions import OfflinePrediction

"""
    {
        "offline_id": 3544,
        "offline_status": 2,
        "dataset_name": "person_pose_data.zip",
        "dataset_id": 5249,
        "model_inst_id": 5828,
        "trial_no": 1,
        "trial_type": 0,
        "eval_metric": {
            "mAP": 0
        }
    }
"""


class TestOfflinePrediction(TestCase):
    def test_list_predictions(self):
        predict = OfflinePrediction.list_predictions(3833)
        for pred in predict:
            detail = pred.get_predict_detail()
            s = detail.get_predict_status()
            self.assertEqual(s, 2)
        print(predict)

    def test_predict(self):
        predict = OfflinePrediction.predict(5734, 5262)
        predict.get_predict_status()
        predict.wait_for_result()
        self.assertIsNot(predict,0)

    def test_get_predict_detail(self):
        predict = OfflinePrediction.get_predict_detail(3672)
        self.assertIsNot(predict.get_predict_status(), 0)
        predict.wait_for_result()
        print(predict.get_predict_status())

    def test_result_download(self):
        predict = OfflinePrediction.result_download(3833, "./report.zip")
        print(predict)

    def test_dataset_download(self):
        predict = OfflinePrediction.dataset_download(3538)
        print(predict)

    def test_delete_predictions(self):
        predict = OfflinePrediction.delete_predictions([3544])
        print(predict)
