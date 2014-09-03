import time
import unittest
from selenium import webdriver
from BaseTest import BaseTest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
from DemoTest import TestSuite1
import sys, getopt

def suite135(self):
#     Runs tests 1,3,5  from TestSuite1
	print 'Runs tests 01, 03, 05'
    suite135 = unittest.TestSuite()
    suite135.addTest(TestSuite1('test_01_try_memeo_modal_is_displayed'))
    # suite135.addTest(TestSuite1('test_03_learn_more_is_displayed_in_delete_user_modal'))
    # suite135.addTest(TestSuite1('test_05_website_footer_is_displayed'))
    return suite135

unittest.TextTestRunner(verbosity=2).run(suite135(2))