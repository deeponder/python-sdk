import unittest
import deepwisdom as dw
import json

dataset_file_path = "/Users/up/Downloads/"
dataset_file_name = "data_upload_test.csv"
project_id = 4087

class TestProject(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestProject, self).__init__(*args, **kwargs)
        api_client = dw.Client(appid=4, api_key="RrTLKoGrgKRXkSJAstcndNLa",
                               secret_key="xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7", domain="http://192.168.50.122:30772")
        dw.set_client(client=api_client)

    def test_create_from_dataset(self):
        """
        in test_main_process.py
        Returns:

        """

    def test_create_from_id(self):
        """
        直接从项目id创建项目对象
        Returns:

        """
        project = dw.Project.create_from_id(project_id)
        self.assertEqual(project.project_id, project_id)  # add assertion here
        # print(project.solution_list()[0].get_detail())
        # return

        srv_list = project.service_list()
        for srv in srv_list:
            detail = srv.get_deployment_detail()
            self.assertEqual(detail.name, srv.service_name)

    def test_trial_list(self):
        """
        获取项目的实验列表
        Returns:

        """
        project = dw.Project.create_from_id(project_id)
        trials = project.trial_list()
        self.assertEqual(trials[0].project_id, project.project_id)

    def test_train(self):
        """
        in test_main_process.py
        Returns:

        """
    def test_solution_list(self):
        """
        项目方案列表
        Returns:

        """
        project = dw.Project.create_from_id(project_id)
        solutions = project.solution_list()
        self.assertEqual(project.project_id, solutions[0].project_id)

    def test_upload_predict_dataset(self):
        project = dw.Project.create_from_id(project_id)
        predict_dataset = project.upload_predict_dataset(dataset_file_path+dataset_file_name)
        self.assertEqual(project.project_id, predict_dataset.project_id)

    def test_custom_model_hp(self):
        ss = dw.SearchSpace.create(0, 1)
        # 修改
        ss.custom_model_hp(["LIGHTGBM", "CATBOOST"])

        flag = True
        for sub_ss in ss.search_space_info:
            if sub_ss["hp_subspace"] == "modeling":
                for hp_obj in sub_ss["hp_values"]["model"]["hp_values"]:
                    if hp_obj["hp_name"] == "RANDOMFOREST":
                        flag = False
                        break

        self.assertEqual(True, flag)

    def test_delete_proj(self):
        dw.Project.delete([4317])

    def test_retrain(self):
        proj = dw.Project.create_from_id(project_id)
        proj.retrain()

if __name__ == '__main__':
    unittest.main()
