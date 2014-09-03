
import time
import unittest
from selenium import webdriver
from BaseTest import BaseTest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
from DemoTest import TestSuite1
import sys, getopt

def suite110(self):
#     Runs all the tests from the TestSuite1 class
	print 'Runs the tests from 1 to 10'
	suite110 = unittest.TestSuite()
	suite110.addTest(unittest.makeSuite(TestSuite1))
	return suite110

unittest.TextTestRunner(verbosity=9).run(suite110(2))