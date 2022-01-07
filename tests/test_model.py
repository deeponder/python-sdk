import unittest
import deepwisdom as dw

project_id = 4087

class TestModel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestModel, self).__init__(*args, **kwargs)
        api_client = dw.Client(appid=4, api_key="RrTLKoGrgKRXkSJAstcndNLa",
                               secret_key="xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7", domain="http://192.168.50.122:30772",
                               admin_domain="http://tianji-admin.dev.deepwisdomai.com")
        dw.set_client(client=api_client)

    def test_download_model(self):
        project = dw.Project.create_from_id(project_id)
        # solutions = project.solution_list()
        recommend_model = project.recommended_select_model()
        recommend_model.download_model()
        # self.assertEqual(project.project_id, 3976)  # add assertion here


if __name__ == '__main__':
    unittest.main()
