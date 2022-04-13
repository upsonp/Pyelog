import unittest
import pyelog


class TestPyelog(unittest.TestCase):

    test_file = None

    def test_create(self):
        pyelog = pyelog(test_file)
        self.assertTrue(False, "you have failed")
