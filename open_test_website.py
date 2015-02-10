import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def open_test_website(self):
#             Opens the demo page for Memeo C1 
        demo_url = 'https://c1.memeo.com/demo'
        driver = self.driver
        driver.get(demo_url)