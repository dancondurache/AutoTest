import time
import unittest
from DemoTest import TestSuite1


def test_suite_1(self):
#     Runs tests 1,3,5  from TestSuite1
	print 'Runs tests 01, 03, 05'
	test_suite_1 = unittest.TestSuite()
	test_suite_1.addTest(TestSuite1('test_01_try_memeo_modal_is_displayed'))
	test_suite_1.addTest(TestSuite1('test_03_learn_more_is_displayed_in_delete_user_modal'))
	test_suite_1.addTest(TestSuite1('test_05_website_footer_is_displayed'))
	return test_suite_1

unittest.TextTestRunner(verbosity=2).run(test_suite_1(2))