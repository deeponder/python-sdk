import unittest
import deepwisdom as dw

dataset_file_path = "/Users/up/Downloads/"
dataset_file_name = "data_upload_test.csv"
dataset_id = 6782

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
        self.assertEqual(dataset_file_name, dataset.file_name)

        datasets = dw.Dataset.dataset_search(dataset_file_name)
        self.assertEqual(dataset.dataset_id, datasets[0].dataset_id)

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
        self.assertEqual(new_name, new_dataset.file_name)

    def test_delete(self):
        """
        数据集删除
        Returns:

        """


if __name__ == '__main__':
    unittest.main()
