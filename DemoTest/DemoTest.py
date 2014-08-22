""" These are the 10 tests:

1. Check for the <Try Memeo C1> popup to be visible
2. Check if the <Try Memeo C1> popup disappears when clicking the <Try it> button
3. Click the <Users> tab link, click the dropdown menu for the first user, click the <Delete> button,
Check that <Learn More> button is visible

4. Check that clicking the <Sign Up> button redirects you to the <Register> page
5. Check that the <Webpage Footer> with version number and copyright info, is visible
6. Click the <Sharing> tab link, click a shared folder, click the <Delete> button,
check if the <Learn More> button's color is red

7. Click the <Sharing> tab link, click a shared folder, click the <Rename> button, rename the folder,
click the <Learn More> button, check if the <Managing Employee..> dialog is displayed

8. Click the <Android Phone> link, check if the dropdown menu text is <Android Phones>
9. Click the <Android Phone> link, click the dropdown menu, uncheck <Android Phones> and check <iPhones/iPods>,
check if iPhones/iPods are displayed
10. Click the <Activity> link, click <Invalid Logins>, click <Map>, check if the map is displayed
"""
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class TestSuite1(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        
        
        
    
    def wait_for_element(self, elem_name = None, elem_id = None, elem_xpath = None):
        """ ^ The wait_for_element method waits for an element (identified by name,id or xpath) to be visible
            to make sure that the webpage has loaded before continuing with the rest of the test. """
        
        contor = 0
        increment = 0.5
        max_duration = 10
        if elem_name == None and elem_xpath == None:
            while contor < max_duration:
                try: 
                    self.driver.find_element_by_id(elem_id)
                    print "The element with element id '%s' has been found" % elem_id
                    return           
                except: 
                    time.sleep(increment)
                    contor = contor + increment
            print "1. The id element was not found"
        
        if elem_name == None and elem_id == None:
            while contor < max_duration:
                try: 
                    self.driver.find_element_by_xpath(elem_xpath) 
                    print "The element with element xpath '%s' has been found" % elem_xpath
                    return
                except: 
                    time.sleep(increment)
                    contor = contor + increment
            print "2. The xpath element was not found" 
            
        if elem_id == None and elem_xpath == None:
            while contor < max_duration:
                try: 
                    self.driver.find_element_by_name(elem_name)
                    print "The element with element name '%s' has been found" % elem_name
                    return
                except: 
                    time.sleep(increment)
                    contor = contor + increment
            print "3. The email element was not found"
    
    def test_try_memeo(self):
        """ Checks if the <Try Memeo C1> popup is displayed"""
        print
        print 'Starting Test1: Is the Try Memeo C1 popup displayed?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        popup = driver.find_element_by_id('e2e-dashboard')
        self.assertTrue(popup.is_displayed(), '"Try Memeo C1" popup is not displayed')
     
    def test_try_it(self):
        """ Checks if the <Try Memeo C1> popup disappears when pressing the Try it button"""
        print
        print 'Starting Test2: Does the popup disappear after after clicking the Try it button?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').send_keys(Keys.RETURN)
        popup = driver.find_element_by_id('e2e-dashboard')
        self.assertFalse(popup.is_displayed(), 'The popup is no longer displayed')
 
           
    def test_learn_more(self):
        """ Checks if the The <Learn More> button is displayed"""
        print
        print 'Starting Test3: Is the Learn More button displayed?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_id('e2e-dashboard').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
        driver.find_element_by_id('menu-users').send_keys(Keys.RETURN)
        """ Sends click on the <USERS> tab link"""
        self.wait_for_element(elem_xpath = '//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/a/span')
        driver.find_element_by_xpath('//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/a/span').click()
        """ Sends click on dropdown menu for the first user in the list"""
        self.wait_for_element(elem_xpath = '//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/ul/li[2]/a')
        driver.find_element_by_xpath('//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/ul/li[2]/a').send_keys(Keys.RETURN)
        """ Sends click on the delete option in the dropdown menu"""
        self.wait_for_element(elem_id = 'deleteButton')
        learn_more = driver.find_element_by_id('deleteButton')
        self.assertTrue(learn_more.is_displayed(), 'The <Learn More> button is NOT displayed')
 
         
    def test_sign_up(self):
        """ Clicks on the <Sign Up> button and checks if the <Company> text field is displayed """           
        print
        print 'Starting Test4: After clicking the Sign Up button am I redirected?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_id('e2e-dashboard').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
        driver.find_element_by_id('demo_signup').send_keys(Keys.RETURN)
        self.wait_for_element(elem_name = 'company_name')
        company = driver.find_element_by_name('company_name')
        self.assertTrue((company.is_displayed), 'The <Company> text field is not displayed')
          
          
    def test_footer(self):
        """ Checks if the webpage footer is displayed"""
        print
        print 'Starting Test5: Is the website footer displayed?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_xpath = '//*[@id="e2e-dashboard"]/div[2]/div[2]/button')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
        self.wait_for_element(elem_id = 'footer')
        footer = driver.find_element_by_id('footer')
        self.assertTrue(footer.is_displayed(), 'The webpage footer is not displayed')
         
             
 
  
    def test_button_color(self):
        """ Checks the color of the <Learn More> button"""
        print
        print 'Starting Test6: Is the color of the Learn More button red?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_id('e2e-dashboard').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
        self.wait_for_element(elem_id = 'menu-sharing')
        driver.find_element_by_id('menu-sharing').send_keys(Keys.RETURN)
        """ Clicks the Sharing tab link"""
        self.wait_for_element(elem_xpath = '//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a')
        driver.find_element_by_xpath('//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a').send_keys(Keys.RETURN)
        """ Finds the first shared folder and clicks on it """
        self.wait_for_element(elem_xpath = '//*[@id="box-actions"]/button[4]')
        driver.find_element_by_xpath('//*[@id="box-actions"]/button[4]').send_keys(Keys.RETURN)
        """ Finds the <Delete> button and clicks on it """
        self.wait_for_element(elem_id = 'deleteButton')
        button_color = driver.find_element_by_id('deleteButton').value_of_css_property('background-color')
        self.assertTrue(button_color == 'rgba(189, 38, 47, 1)', 'The color of the button is not the right one')
        print button_color
         
    def test_manage_dialog(self):
        """ Checks if the <Managing Employee..> dialog is displayed"""
        print
        print 'Starting Test7: Is the <Managing Employee..> dialog displayed?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
        self.wait_for_element(elem_id = 'menu-sharing')
        driver.find_element_by_id('menu-sharing').send_keys(Keys.RETURN)
        """ Clicks the Sharing tab link"""
        self.wait_for_element(elem_xpath = '//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a')
        driver.find_element_by_xpath('//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a').send_keys(Keys.RETURN)
        """ Finds the first shared folder and clicks on it """
        self.wait_for_element(elem_xpath = '//*[@id="box-actions"]/button[3]')
        driver.find_element_by_xpath('//*[@id="box-actions"]/button[3]').send_keys(Keys.RETURN)
        """ Finds the <Rename> button and clicks on it """
          
        time.sleep(2)
        learn_more = driver.find_element_by_xpath('//*[@id="e2e-shared_folder_rename"]/div[2]/div[2]/div/button[2]')
        learn_more.click()
        """ Finds the <Learn More> button and clicks on it"""
           
        self.wait_for_element(elem_xpath = '//*[@id="e2e-devices"]/div[2]/div[2]/button[1]')
        manage_dialog = driver.find_element_by_id('e2e-devices')
        self.assertTrue(manage_dialog.is_displayed(), 'The <Manage Employee> dialog is NOT displayed')
         
    def test_android_phones(self):
        print
        print 'Starting Test8: Is the <Android Phones> dropdown menu displayed?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
           
        self.wait_for_element(elem_xpath = '//*[@id="e2e-dashboard-devices"]/div/div[5]/div/div[1]/a/span/i[2]')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard-devices"]/div/div[5]/div/div[1]/a/span/i[2]').click()
        """ Clicks on <Android Phones> link """
        self.wait_for_element(elem_xpath = '//*[@id="types_filter"]/button')
        android_phones = driver.find_element_by_xpath('//*[@id="types_filter"]/button')
        self.assertTrue(android_phones.is_displayed(), 'The <Android Phones> dropdown menu is NOT displayed')
         
         
    def test_iphones(self):
        """ Checks if the iPhone links are displayed """
        print
        print 'Starting Test9: Are the <iPhone links> displayed?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
          
        driver.find_element_by_xpath('//*[@id="e2e-dashboard-devices"]/div/div[5]/div/div[1]/a/span/i[2]').click()
        self.wait_for_element(elem_xpath = '//*[@id="types_filter"]/button')
        driver.find_element_by_xpath('//*[@id="types_filter"]/button').click()
        driver.find_element_by_xpath('//*[@id="types_filter"]/ul/li[3]/a/span[2]').click()
        driver.find_element_by_xpath('//*[@id="types_filter"]/ul/li[5]/a/span[2]').click()
        driver.find_element_by_id('content').click()
        self.wait_for_element(elem_xpath = '//*[@id="devices"]/tbody/tr[1]/td[2]/div/div[2]/span[1]/a')
        iphone = driver.find_element_by_partial_link_text('s iPhone ')
        self.assertTrue(iphone.is_displayed(), 'The <iPhone> links are NOT displayed')
          
    def test_map(self):
        """ Checks if the Map is displayed """
        print
        print 'Starting Test10: Is the map displayed?'
        driver = self.driver
        driver.get('https://c1.memeo.com/demo')
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').send_keys(Keys.RETURN)
        """ Sends click on the <Try it> button"""
         
        driver.find_element_by_id('menu-activity').click()
        self.wait_for_element(elem_xpath = '//*[@id="custom-reports"]/ul/li[6]/a')
        driver.find_element_by_xpath('//*[@id="custom-reports"]/ul/li[6]/a').click()
         
        self.wait_for_element(elem_id = 'activityMap_button')
        driver.find_element_by_id('activityMap_button').click()
         
        time.sleep(3)
        map = driver.find_element_by_id('e2e-map_list')
        self.assertTrue(map.is_displayed(), 'The map is NOTd displayed')
        
    def tearDown(self):
        self.driver.quit()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite1)
unittest.TextTestRunner(verbosity=2).run(suite)
             
if __name__ == "__main__":
    unittest.main()

