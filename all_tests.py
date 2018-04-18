import unittest
from tests.test_client import ConnectionTest
from tests.test_client import TestHeartbeat  


def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(ConnectionTest())
    suite.addTest(TestHeartbeat())
    return suite

if __name__ == '__main__':
    suite = create_suite()

    runner = unittest.TextTestRunner()
    runner.run(suite)

