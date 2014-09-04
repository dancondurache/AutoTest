import time
import unittest
from DemoTest import TestSuite1

def test_suite_2(self):
#     Runs all the tests from the TestSuite1 class
	print 'Runs the tests from 1 to 10'
	test_suite_2 = unittest.TestSuite()
	test_suite_2.addTest(unittest.makeSuite(TestSuite1))
	return test_suite_2

unittest.TextTestRunner(verbosity=9).run(test_suite_2(2))