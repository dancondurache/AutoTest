import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
    
def custom_is_visible(self, elem_name = None, elem_id = None, elem_xpath = None):
    
    if elem_name == None and elem_id == None:
        
        try:
            self.driver.find_element_by_xpath(elem_xpath)
        except:
            raise (NoSuchElementException, '1. The element with that XPath does not exist')
             
        
        try:
            self.assertIn('block', self.driver.find_element_by_xpath(elem_xpath).get_attribute('style'),
                         '1.The popup Is Not visible')
        except: 
            raise (NoSuchAttributeException, '2. The element does not have a <Style> Attribute') 
            
    if elem_name == None and elem_xpath == None:
        
        try:
            self.driver.find_element_by_id(elem_id)
        except:
            raise (NoSuchElementException, '1. The element with that Id does not exist')
        
        try:
            self.assertIn('block', self.driver.find_element_by_id(elem_id).get_attribute('style'),
                         '1.The popup Is Not visible')
        except: 
            raise (NoSuchAttributeException, '2. The element does not have a <Style> Attribute') 
    
    if elem_xpath == None and elem_id == None:
        
        try:
            self.driver.find_element_by_name(elem_name)
        except:
            raise (NoSuchElementException, '1. The element with that Name does not exist')
        
        try:
            self.assertIn('block', self.driver.find_element_by_name(elem_name).get_attribute('style'),
                         '1.The popup Is Not visible')
        except: 
            raise (NoSuchAttributeException, '2. The element does not have a <Style> Attribute') 