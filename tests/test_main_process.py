import unittest
import deepwisdom as dw

dataset_file_path = "/Users/up/Downloads/"
dataset_file_name = "data_upload_test.csv"
train_succ_status = 2


class TestMainProcess(unittest.TestCase):
    def test_main_process(self):
        # # 数据集
        dataset = dw.Dataset.create_from_file(dataset_file_path+dataset_file_name, 0)
        self.assertEqual(dataset.name, dataset_file_name)
        # # 项目
        primary_label = "is_marry"
        project_name = "SDK-MAIN-PROCESS-TEST"
        train_setting = dw.TrainSetting(training_program="zhipeng", max_trials=3)
        settings = dw.AdvanceSetting("off", "ga", 6571, target_train=train_setting)
        dataset_id = dataset.dataset_id
        # dataset_id = 6062
        project = dw.Project.create_from_dataset(name=project_name, dataset_id=dataset_id, model_type=0, task_type=0,
                                         scene=1, primary_label=primary_label, primary_main_time_col="", id_cols="", advance_settings=settings)
        self.assertEqual(project.name, project_name)
        ## 训练
        project.wait_train()
        self.assertEqual(train_succ_status, project.status)
        solutions = project.solution_list()
        solution_one = solutions[0]
        self.assertEqual(solution_one.project_id, project.project_id)

        models = project.get_select_models(solution_one.trial_no, solution_one.trial_type)
        model_one = models[0]
        self.assertEqual(model_one.project_id, project.project_id)


if __name__ == '__main__':
    unittest.main()
