import unittest
import deepwisdom as dw


class TestProject(unittest.TestCase):
    def test_create_from_id(self):
        project = dw.Project.create_from_id(4069)
        self.assertEqual(project.project_id, 4069)  # add assertion here


if __name__ == '__main__':
    unittest.main()
