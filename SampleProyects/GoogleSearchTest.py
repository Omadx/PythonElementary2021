from selenium import webdriver

import unittest

class DuckDuckGo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="c:\seleniumBrowserDrivers\geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # def test_search_automationsbasic(self):
    #     self.driver.get("https://duckduckgo.com/")
    #     self.driver.find_element_by_name("q").send_keys("Automation Step by Step")
    #     self.driver.find_element_by_id("search_button_homepage").click()

    def test_search_automations_Hispatec(self):
        self.driver.get("https://duckduckgo.com/")
        self.driver.find_element_by_name("q").send_keys("Hispatec")
        self.driver.find_element_by_id("search_button_homepage").click()

    # @classmethod
    # def tearDownClass(cls):
    #     # cls.driver.close()
    #     # cls.driver.quit()
    #     print("test completed")
