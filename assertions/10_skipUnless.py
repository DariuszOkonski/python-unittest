import sys
import unittest

class TestClass(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('linus'), 'Requires linux')
    def test_case_2(self):
        self.assertEqual('aws'.upper(), 'AWS')

    @unittest.skipUnless(sys.platform.startswith('win'), 'Requires windows')
    def test_case_3(self):
        self.assertEqual('aws'.upper(), 'AWS')