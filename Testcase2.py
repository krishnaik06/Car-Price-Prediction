# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:13:04 2020

@author: RAHUL JAIN
"""

import unittest
from selenium import webdriver
import time

class logintests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(250)
        cls.driver.maximize_window()
    
    
    
    def test__web(self):
        self.driver.get("http://127.0.0.1:5000/")
        #print("Title of the page is :"+self.driver.title)
        self.driver.find_element_by_id("first").send_keys("2019")
        self.driver.find_element_by_id("second").send_keys("8")
        self.driver.find_element_by_id("third").send_keys("20000")
        self.driver.find_element_by_id("fourth").send_keys("1")
        self.driver.find_element_by_id("fuel").send_keys("Diesel")
        #self.driver.find_element_by_xpath("//select[@id='fuel']/option[value()='Petrol']").click()
        self.driver.find_element_by_id("resea").send_keys("Individual")
        #self.driver.find_element_by_xpath("//select[@id='resea']/option[value()='Individual']").click()
        #self.driver.find_element_by_xpath("//select[@id='research']/option[value()='Mannual']").click()
        self.driver.find_element_by_id("research").send_keys("Manual Car")
        self.driver.find_element_by_id("sub").click()
      
        time.sleep(20)
        
        
        
    @classmethod
    def tearDownClass(cls):
        
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        


        
if __name__=="__main__":
    unittest.main()
