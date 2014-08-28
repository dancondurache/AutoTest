""" These are the 10 tests:

1. Check for the <Try Memeo C1> popup to be visible
2. Check if the <Try Memeo C1> popup disappears when clicking the TryIt button
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


class TestSuite1(unittest.TestCase):
    from custom_is_visible import custom_is_visible
    from wait_for_element import wait_for_element
    from open_test_website import open_test_website
    from check_footer import check_footer
    
    def setUp(self):
        self.driver = webdriver.Firefox()
                        
    def test_try_memeo_modal_is_displayed(self):
#         Checks if the <Try Memeo C1> popup is displayed
        print
        print 'Starting Test1: Is the Try Memeo C1 popup displayed?'
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        self.custom_is_visible(elem_xpath = '//*[@id="ng-app"]/body/div[5]')
           
    def test_try_memeo_modal_closes_on_try_it_click(self):
#         Checks if the TryMemeoC1 popup disappears when pressing the TryIt button
        print
        print 'Starting Test2: Does the popup disappear after after clicking the Try it button?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').click()
        popup = driver.find_element_by_id('e2e-dashboard')
        self.assertFalse(popup.is_displayed(), 'The TryMemeoC1 modal is no longer displayed')
       
                 
    def test_learn_more_is_displayed_in_delete_user_modal(self):
#          Checks if the LearnMore button is displayed
            
        print
        print 'Starting Test3: Is the Learn More button displayed?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_id('e2e-dashboard').click()
#         Clicks on the TryIt button
        driver.find_element_by_id('menu-users').click()
#         Clicks on the USERS link
        self.wait_for_element(elem_xpath = '//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/a/span')
        driver.find_element_by_xpath('//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/a/span').click()
#         Clicks the dropdown menu for the first user in the list
        self.wait_for_element(elem_xpath = '//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/ul/li[2]/a')
        driver.find_element_by_xpath('//*[@id="userTable"]/tbody/tr[1]/td[1]/div/div/ul/li[2]/a').click()
#         Clicks on the delete option in the dropdown menu
        self.wait_for_element(elem_id = 'deleteButton')
        learn_more = driver.find_element_by_id('deleteButton')
        self.assertTrue(learn_more.is_displayed(), 'The LearnMore button from the DeleteUser modal IS NOT displayed')
       
               
    def test_signup_redirects_to_register_url(self):
#         Checks if the SignUp button redirects to RegisterUrl https://c1.memeo.com/app_js/register          
        print
        print 'Starting Test4: After clicking the Sign Up button am I redirected?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_id('e2e-dashboard').click()
#         Clicks on the TryIt button
        driver.find_element_by_id('demo_signup').click()
        self.wait_for_element(elem_name = 'company_name')
        register_url = self.driver.current_url 
        print register_url
        self.assertEqual(register_url, 'https://c1.memeo.com/app_js/register', 'The SignUp button DOES NOT redirect to the RegisterUrl https://c1.memeo.com/app_js/register')
                
                
    def test_website_footer_is_displayed(self):
#         Checks if the webpage footer is displayed
        print
        print 'Starting Test5: Is the website footer displayed?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_xpath = '//*[@id="e2e-dashboard"]/div[2]/div[2]/button')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').click()
#         Clicks on the TryIt button
        self.wait_for_element(elem_xpath = '//*[@id="footer"]')
        self.check_footer()


    def test_learn_more_is_red_in_delete_folder_modal(self):
#         Checks the color of the LearnMore button
        print
        print 'Starting Test6: Is the color of the Learn More button red?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_id('e2e-dashboard').click()
#         Clicks on the TryIt button
        self.wait_for_element(elem_id = 'menu-sharing')
        driver.find_element_by_id('menu-sharing').click()
#         Clicks the Sharing tab link
        self.wait_for_element(elem_xpath = '//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a')
        driver.find_element_by_xpath('//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a').click()
        """ Finds the first shared folder and clicks on it """
        self.wait_for_element(elem_xpath = '//*[@id="box-actions"]/button[4]')
        driver.find_element_by_xpath('//*[@id="box-actions"]/button[4]').click()
#         Clicks the Delete button 
        self.wait_for_element(elem_id = 'deleteButton')
        button_color = driver.find_element_by_id('deleteButton').value_of_css_property('background-color')
        self.assertTrue(button_color == 'rgba(189, 38, 47, 1)', 'The color of the LearnMore button from DeleteSharedFolder modal IS NOT red')
        print button_color
        
               
    def test_manage_employee_is_displayed_in_rename_folder_modal(self):
#         Checks if the ManagingEmployee dialog is displayed
        print
        print 'Starting Test7: Is the <Managing Employee..> dialog displayed?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').click()
#         Clicks on the TryIt button
        self.wait_for_element(elem_id = 'menu-sharing')
        driver.find_element_by_id('menu-sharing').click()
#         Clicks the Sharing tab link
        self.wait_for_element(elem_xpath = '//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a')
        driver.find_element_by_xpath('//*[@id="internalSharesTable"]/tbody/tr[1]/td[1]/a').click()
#         Clicks the first SharedFolder
        self.wait_for_element(elem_xpath = '//*[@id="box-actions"]/button[3]')
        driver.find_element_by_xpath('//*[@id="box-actions"]/button[3]').click()
#         Clicks the Rename button
        time.sleep(2)
        learn_more = driver.find_element_by_xpath('//*[@id="e2e-shared_folder_rename"]/div[2]/div[2]/div/button[2]')
        learn_more.click()
#         Clicks the LearnMore button
        self.wait_for_element(elem_xpath = '//*[@id="e2e-devices"]/div[2]/div[2]/button[1]')
        manage_dialog = driver.find_element_by_id('e2e-devices')
        self.custom_is_visible(elem_xpath = '//*[@id="ng-app"]/body/div[6]')
        
               
    def test_android_phones_is_displayed_in_dropdown_menu(self):
        print
        print 'Starting Test8: Is the <Android Phones> dropdown menu displayed?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').click()
#          Clicks the TryIt button
        self.wait_for_element(elem_xpath = '//*[@id="e2e-dashboard-devices"]/div/div[5]/div/div[1]/a/span/i[2]')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard-devices"]/div/div[5]/div/div[1]/a/span/i[2]').click()
#          Clicks AndroidPhones link
        self.wait_for_element(elem_xpath = '//*[@id="types_filter"]/button')
        android_phones = driver.find_element_by_xpath('//*[@id="types_filter"]/button')
        self.assertTrue(android_phones.is_displayed(), 'The AndroidPhones IS NOT displayed in the dropdown menu')
         
                
    def test_iphones_are_displayed_in_devices(self):
#          Checks if the iPhone links are displayed
        print
        print 'Starting Test9: Are the <iPhone links> displayed?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').click()
#          Clicks the TryIt button
        driver.find_element_by_xpath('//*[@id="e2e-dashboard-devices"]/div/div[5]/div/div[1]/a/span/i[2]').click()
        self.wait_for_element(elem_xpath = '//*[@id="types_filter"]/button')
        driver.find_element_by_xpath('//*[@id="types_filter"]/button').click()
        driver.find_element_by_xpath('//*[@id="types_filter"]/ul/li[3]/a/span[2]').click()
        driver.find_element_by_xpath('//*[@id="types_filter"]/ul/li[5]/a/span[2]').click()
        driver.find_element_by_id('content').click()
        self.wait_for_element(elem_xpath = '//*[@id="devices"]/tbody/tr[1]/td[2]/div/div[2]/span[1]/a')
        iphone = driver.find_element_by_partial_link_text('s iPhone ')
        self.assertTrue(iphone.is_displayed(), 'The iPhone/iPod links ARE NOT displayed in iPhone/iPod devices')
         
                
    def test_map_is_displayed_in_invalid_login_activity(self):
#          Checks if the Map is displayed
        print
        print 'Starting Test10: Is the map displayed?'
        driver = self.driver
        self.open_test_website()
        self.wait_for_element(elem_id = 'e2e-dashboard')
        driver.find_element_by_xpath('//*[@id="e2e-dashboard"]/div[2]/div[2]/button').click()
#         Clicks the TryIt button
        driver.find_element_by_id('menu-activity').click()
        self.wait_for_element(elem_xpath = '//*[@id="custom-reports"]/ul/li[6]/a')
        driver.find_element_by_xpath('//*[@id="custom-reports"]/ul/li[6]/a').click()
        self.wait_for_element(elem_id = 'activityMap_button')
        driver.find_element_by_id('activityMap_button').click()
        time.sleep(3)
        map = driver.find_element_by_id('e2e-map_list')
        self.custom_is_visible(elem_xpath = '//*[@id="ng-app"]/body/div[7]')                                        

        
    def tearDown(self):
        self.driver.quit()

# suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite1)
# unittest.TextTestRunner(verbosity=2).run(suite)
# ^ Runs tests from a certain TestSuite
             
if __name__ == "__main__":
    unittest.main()

