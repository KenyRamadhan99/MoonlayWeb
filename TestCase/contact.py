import sys
sys.path.append('C:/Users/Qoin/OneDrive - PT. Loyalty Program Indonesia/Documents/MoonlayWeb')
from selenium import webdriver
import unittest
from PageObject.Page.elementObject import contactLocator
from TestData.dataTest import dataForm
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner
       
class TestCreate(unittest.TestCase): 
   
    @classmethod
    def setUp(cls): 
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(dataForm.URL)
        
    def test_create_success_contact_form(self): 
       
        driver = self.driver
        inputContactForm = contactLocator(driver)
        inputContactForm.inputFirstName(dataForm.FirstName)
        inputContactForm.inputLastName(dataForm.LastName)
        inputContactForm.inputEmail(dataForm.Email)
        inputContactForm.inputPhoneNumber(dataForm.PhoneNumber)
        inputContactForm.inputServices(dataForm.Services)
        inputContactForm.inputMessage(dataForm.Message)
        inputContactForm.submit()
        inputContactForm.successInput()
        

    def test_create_blank_contact_form(self): 
       
        driver = self.driver
        inputContactForm = contactLocator(driver)
        inputContactForm.submit()
        inputContactForm.failedSubmit()

       

    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")


if __name__ == "__main__": 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Qoin/OneDrive - PT. Loyalty Program Indonesia/Documents/MoonlayWeb/Reports"))          
          


    
