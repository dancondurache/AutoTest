import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def check_footer(self):
        driver = self.driver 
        try:       
            self.driver.find_element_by_xpath('//*[@id="footer"]') 
        except:
            raise (NoSuchElement, 'The Footer Is Not displayed')
        
        try:
            self.driver.find_element_by_xpath('//*[@id="footer"]/div[1]') 
        except:
            raise (NoSuchElement, 'The Version Number Is Not displayed')
        
        try:
            self.driver.find_element_by_xpath('//*[@id="footer"]/div[2]')
        except:
            raise (NoSuchElement, 'The Copyright Info Is Not displayed')