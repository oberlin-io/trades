# https://docs.python.org/3/library/unittest.html#unittest.TestCase

import unittest
import yf_client
import pg_client

class TestYFClient(unittest.TestCase):

    def test_get_historical(self):
        self.assertIsInstance(
            yf_client.YFClient().get_historical('TSLA', 'US'),
            str)

class TestPGClient(unittest.TestCase):

    def test_get_historical(self):
        self.assertIsInstance(
            yf_client.YFClient().get_historical('TSLA', 'US'),
            str)


if __name__ == '__main__':
    unittest.main()
