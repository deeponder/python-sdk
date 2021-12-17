import unittest
import deepwisdom as dw


class TestProject(unittest.TestCase):
    def test_create_from_id(self):
        project = dw.Project.create_from_id(3976)
        self.assertEqual(project.project_id, 3976)  # add assertion here
        srv_list = project.service_list()
        print(srv_list)
        for srv in srv_list:
            detail = srv.get_deployment_detail()
            self.assertEqual(detail.name, srv.service_name)
        pred_list = project.offline_prediction_list()
        print(pred_list)
        for pred in pred_list:
            prediction = pred.predict()
            print(prediction)


if __name__ == '__main__':
    unittest.main()
