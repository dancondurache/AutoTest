import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
import unittest

class BaseTest(unittest.TestCase):
    
    def open_test_website(self):
#         Opens the demo page for Memeo C1
#         driver = webdriver.PhantomJS()
#         driver.set_window_size(1280, 900)
        driver = self.driver
        demo_url = 'https://c1.memeo.com/demo'
        driver.get(demo_url)
       
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
        
    def wait_for_element(self, elem_name = None, elem_id = None, elem_xpath = None):
        """ The wait_for_element method waits for an element (identified by name,id or xpath) to be visible
            to make sure that the webpage has loaded before continuing with the rest of the test. 
        """
        
        contor = 0
        increment = 0.5
        max_duration = 10
        if elem_name == None and elem_xpath == None:
            while contor < max_duration:
                try: 
                    self.driver.find_element_by_id(elem_id)
#                         print "The element with the Id '%s' has been found" % elem_id
                    return           
                except: 
                    time.sleep(increment)
                    contor = contor + increment
            print "1. The id element was not found"
        
        if elem_name == None and elem_id == None:
            while contor < max_duration:
                try: 
                    self.driver.find_element_by_xpath(elem_xpath) 
#                         print "The element with the XPath '%s' has been found" % elem_xpath
                    return
                except: 
                    time.sleep(increment)
                    contor = contor + increment
            print "2. The xpath element was not found" 
            
        if elem_id == None and elem_xpath == None:
            while contor < max_duration:
                try: 
                    self.driver.find_element_by_name(elem_name)
#                         print "The element with the Name '%s' has been found" % elem_name
                    return
                except: 
                    time.sleep(increment)
                    contor = contor + increment
            print "3. The email element was not found"
            
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

    def tearDown(self):
        self.driver.quit()
