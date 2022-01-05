import unittest
import deepwisdom as dw

dataset_file_path = "/Users/up/Downloads/"
dataset_file_name = "data_upload_test.csv"
dataset_id = 6999

class TestDataset(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDataset, self).__init__(*args, **kwargs)
        api_client = dw.Client(appid=4, api_key="RrTLKoGrgKRXkSJAstcndNLa",
                               secret_key="xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7", domain="http://192.168.50.122:30772")
        dw.set_client(client=api_client)

        # self.dataset = dw.Dataset.create_from_file(dataset_file_path + dataset_file_name, 0)

    def test_create_from_file(self):
        """
        从本地文件创建数据集
        Returns:

        """

        # api_client = dw.Client(appid=4, api_key="RrTLKoGrgKRXkSJAstcndNLa",
        #                        secret_key="xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7", domain="http://192.168.50.122:30772")
        # dw.set_client(client=api_client)
        dataset = dw.Dataset.create_from_file(dataset_file_path + dataset_file_name, 0)
        self.assertEqual(dataset_file_name, dataset.dataset_name)

        datasets = dw.Dataset.dataset_search(dataset_file_name)
        self.assertEqual(dataset.dataset_id, datasets[0].dataset_id)

    def test_create_from_data_source(self):
        """
        从数据源创建
        Returns:

        """
        datasets = dw.Dataset.create_from_data_source(
            '{"host":"192.168.50.26","port":"3306","user":"autotables","password":"v9rf+MmPdzWYF7jmT5uKsD0UltPBVk8l4FOhRkySTJU=","db":"","encoding":"utf8","passwordCustom":"v9rf+MmPdzWYF7jmT5uKsD0UltPBVk8l4FOhRkySTJU="}',
            0,
            1,
            '[{"autotables":[{"table_name":"dataset_update_record"},{"table_name":"scene"}]}]'
        )
        flag = False
        for dataset in datasets:
            if dataset.dataset_name == "dataset_update_record":
                flag = True
        self.assertEqual(True, flag)


    def test_modify_eda(self):
        dataset = dw.Dataset.create_from_dataset_id(dataset_id)
        eda = dataset.get_eda()
        # print(eda.loc["is_marry", "dtype"])
        eda.loc["is_marry", "dtype"] = "c"
        # print(eda.to_json(orient='split'))
        dataset.modify_eda(eda)
        new_eda = dataset.get_eda()
        self.assertEqual("c", new_eda.loc["is_marry", "dtype"])

    def test_create_from_dataset_id(self):
        print(dataset_id)
        dataset = dw.Dataset.create_from_dataset_id(dataset_id)

        self.assertEqual(dataset_id, dataset.dataset_id)

    def test_dataset_search(self):
        """
        数据集模糊搜索
        in test_create_from_file
        Returns:

        """

    def test_modify(self):
        """
        数据集修改，目前支持名称修改
        Returns:

        """
        new_name = "new_"+dataset_file_name
        dw.Dataset.modify_dataset(dataset_id, new_name)
        new_dataset = dw.Dataset.create_from_dataset_id(dataset_id)
        self.assertEqual(new_name, new_dataset.dataset_name)

    def test_delete(self):
        """
        数据集删除
        Returns:

        """


if __name__ == '__main__':
    unittest.main()
