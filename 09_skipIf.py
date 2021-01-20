from datetime import date
import unittest


class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipIf(date.today().day % 2 == 0, 'keeping odd days')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')
