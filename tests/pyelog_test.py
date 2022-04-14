import unittest

from pyelog import Pyelog

test_file = r"data/elog_test.cfg"

EXPECTED_PORT_KEY = "port"

EXPECTED_NUMBER_OF_LOGBOOKS = 4
EXPECTED_LOG_BOOK = "Itinerary"
EXPECTED_ITINERARY_SHOW_TEXT_KEY = "Show text"
EXPECTED_ITINERARY_SHOW_TEXT_VALUE = '1'


class TestPyelog(unittest.TestCase):

    def test_create(self):
        pyelog = Pyelog(test_file)

        self.assertIsNotNone(pyelog, "The pyelog object was not created")
        self.assertIsNotNone(pyelog.global_var, "The global variables have not been created")
        self.assertIsNotNone(pyelog.logbook, "The logbook dictionaries have not been created")

        # We'll have to expand this later to check for other variables, but at the moment I'm only interested
        # in *if* variables were loaded into the global dictionary
        self.assertTrue(EXPECTED_PORT_KEY in pyelog.global_var, "port key was not set")

        self.assertEqual(EXPECTED_NUMBER_OF_LOGBOOKS, len(Pyelog.logbook.keys()))
        self.assertTrue(EXPECTED_ITINERARY_SHOW_TEXT_KEY in Pyelog.logbook[EXPECTED_LOG_BOOK])
        self.assertEqual(EXPECTED_ITINERARY_SHOW_TEXT_VALUE,
                         Pyelog.logbook[EXPECTED_LOG_BOOK][EXPECTED_ITINERARY_SHOW_TEXT_KEY])
