from unittest import TestCase
from .predict import OfflinePrediction


class TestOfflinePrediction(TestCase):
    def test_list_predictions(self):
        offline_pred = OfflinePrediction(appId=4, apiKey="RrTLKoGrgKRXkSJAstcndNLa",
                                         secretKey="xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7",
                                         reqAddr="http://192.168.50.122:30772")
        result = offline_pred.get_predict_detail(3080)
        print(result)
