import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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