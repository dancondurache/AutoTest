import time
import unittest
from DemoTest import TestSuite1
import HTMLTestRunner

def test_suite_2(self):
	test_suite_2 = unittest.TestSuite()
	test_suite_2.addTest(unittest.makeSuite(TestSuite1))
	return test_suite_2

def run(test_suite_2, report = "Results/test_results.html"):
	with open(report, "w") as f:
		HTMLTestRunner.HTMLTestRunner(
					stream = f,
					title = 'Test Suite 1',
					verbosity = 2,
					description = 'Runs the tests from 1 to 10'
					).run(test_suite_2)

if __name__ == "__main__":
	run(test_suite_2(2))