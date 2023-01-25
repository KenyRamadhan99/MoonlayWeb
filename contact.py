from selenium import webdriver
import unittest
import time
from random_username.generate import generate_username # fitur dari py buat manggil random username
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class TestCreate(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_create_success_contact_form(self): 
        browser = self.browser
        browser.get("https://moonlay.com/contact-us/")  # buka situs
        browser.maximize_window()
        browser.implicitly_wait(5)

        # dibawah ini untuk input form 
        browser.find_element(By.ID,"ff_3_names_first_name_").send_keys("Kenny Testing")
        time.sleep(2)
        browser.find_element(By.ID,"ff_3_names_last_name_").send_keys("Testing") 
        time.sleep(2)
        browser.find_element(By.ID,"ff_3_email").send_keys("kenny@gmail.com") 
        time.sleep(2)
        browser.find_element(By.ID,"ff_3_phone_number").send_keys("12334454") 
        time.sleep(2)
        service_select = Select(browser.find_element(By.ID,"ff_3_dropdown"))
        service_select.select_by_visible_text('Brain Resources')
        time.sleep(2)

        browser.find_element(By.ID,"ff_3_message").send_keys("Testing") 
        time.sleep(2)
        
        #submit data 
        browser.find_element(By.XPATH,"//*[@id='fluentform_3']/div[6]/button" ).click() #klik submit
        time.sleep(2)

        # Validasi
        create_success = browser.find_element(By.ID,"fluentform_3_success").text
        self.assertEqual(create_success,"Thank you for your message. We will get in touch with you shortly")
        print(create_success)

    def test_create_blank_contact_form(self): 
        browser = self.browser 
        browser.get("https://moonlay.com/contact-us/")  # buka situs
        browser.maximize_window()
        browser.implicitly_wait(5)
    
        # submit data 
        browser.find_element(By.XPATH,"//*[@id='fluentform_3']/div[6]/button" ).click() #klik submit
        time.sleep(5)

        browser.execute_script("Alert('Form Stil Empty')")
        browser.implicitly_wait(5)


if __name__ == "__main__": 
    unittest.main()          
          


    
