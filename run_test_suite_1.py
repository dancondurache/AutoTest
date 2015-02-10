import time
import unittest
from DemoTest import TestSuite1
import HTMLTestRunner


def test_suite_1(self):
	test_suite_1 = unittest.TestSuite()
	test_suite_1.addTest(TestSuite1('test_01_try_memeo_modal_is_displayed'))
	test_suite_1.addTest(TestSuite1('test_03_learn_more_is_displayed_in_delete_user_modal'))
	test_suite_1.addTest(TestSuite1('test_05_website_footer_is_displayed'))
	return test_suite_1

def run(test_suite_1, report = "C:/Program Files (x86)/Jenkins/jobs/Results/test_results.html"):
	with open(report, "w") as f:
		HTMLTestRunner.HTMLTestRunner(
					stream = f,
					title = 'Test Suite 1',
					verbosity = 2,
					description = 'Runs tests 1,3,5  from TestSuite1'
					).run(test_suite_1)

if __name__ == "__main__":
	run(test_suite_1(2))