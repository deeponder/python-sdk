import unittest
import deepwisdom as dw


class TestProject(unittest.TestCase):
    def test_create_from_id(self):
        api_client = dw.Client(appid=4, api_key="RrTLKoGrgKRXkSJAstcndNLa",
                               secret_key="xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7", domain="http://192.168.50.122:30772")
        dw.set_client(client=api_client)
        project = dw.Project.create_from_id(3976)
        self.assertEqual(project.project_id, 3976)  # add assertion here


if __name__ == '__main__':
    unittest.main()
