import sys
sys.path.append('C:/Users/Qoin/OneDrive - PT. Loyalty Program Indonesia/Documents/MoonlayWeb')
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObject.Locator.locator import Locators
from TestData.dataTest import dataForm

class contactLocator():

    def __init__(self,driver):
        self.driver = driver


        self.getInputFirstName = Locators.getInputFirstName
        self.getInputLastName = Locators.getInputLastName
        self.getInputEmail = Locators.getInputEmail
        self.getInputPhoneNumber = Locators.getInputPhoneNumber
        self.getSelectDropdown = Locators.getSelectDropdown
        self.getInputMessage = Locators.getInputMessage
        self.getSubmitButton = Locators.getSubmitButton
        self.getSuccessWarning = Locators.getSuccessWarning
    
    def inputFirstName(self,firstName):
        self.driver.find_element(By.ID,self.getInputFirstName).send_keys(firstName)
        time.sleep(2)

    def inputLastName(self,lastName):
        self.driver.find_element(By.ID,self.getInputLastName).send_keys(lastName) 
        time.sleep(2)

    def inputEmail(self,email):
        self.driver.find_element(By.ID,self.getInputEmail).send_keys(email) 
        time.sleep(2)

    def inputPhoneNumber(self,phoneNumber):
        self.driver.find_element(By.ID,self.getInputPhoneNumber ).send_keys(phoneNumber) 
        time.sleep(2)

    def inputServices(self,services):
        service_select = Select(self.driver.find_element(By.ID,self.getSelectDropdown))
        service_select.select_by_visible_text(services)
        time.sleep(2)

    def inputMessage(self,message):
        self.driver.find_element(By.ID,self.getInputMessage).send_keys(message)
        self.driver.get_screenshot_as_file("C:/Users/Qoin/OneDrive - PT. Loyalty Program Indonesia/Documents/MoonlayWeb/Screenshoot") 
        time.sleep(2)
        

    def submit(self):
        self.driver.find_element(By.XPATH,self.getSubmitButton).click() 
        time.sleep(2)
    def successInput(self):

        if self.driver.find_element(By.ID,self.getSuccessWarning).text==dataForm.SuccessMessage:
            print("Input Form Contact Success")
        else:
            print("Failed To Create Data")

        
    def failedSubmit(self):    
        
        if self.driver.find_element(By.CSS_SELECTOR,".error.text-danger").is_displayed():
            self.driver.get_screenshot_as_file("C:/Users/Qoin/OneDrive - PT. Loyalty Program Indonesia/Documents/MoonlayWeb/Screenshoot") 
        else:
            print("Failed")

