import logging
import os
import json

import deepwisdom as dw


if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO)
    api_client = dw.Client()
    dw.set_client(api_client)
    dataset = dw.Dataset.create_from_file("/Users/up/Downloads/data_upload_test.csv", 0)
    print(dataset.name)

    train_setting = dw.TrainSetting(training_program="huangzhi")
    settings = dw.AdvanceSetting("off", "ga", 6571, target_train=train_setting)
    project = dw.Project.create_from_dataset(dataset_id=5584, model_type=0, task_type=0,
                                             scene=1, primary_label="is_marry", primary_main_time_col="", id_cols="", advance_settings=settings)

    print(project.project_id)

#     4066

    # project = dw.Project.create_from_id(4069)
    # print(project.name)
    # # # project.train()
    # # print(project.check_train_finish())
    # #
    # solutions = project.solution_list()
    # #
    # models = project.get_select_models(solutions[0].trial_no, solutions[0].trial_type)
    # #
    # print(models[0].project_id)
    #
    # print(project.trial_list()[0].trial_metric.performance_metrics.fps)





