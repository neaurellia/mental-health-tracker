import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

class ExampleFunctionalTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_handling_text_is_correct(self):
        self.browser.get("http://catherine-aurellia-mental-health-tracker.pbp.cs.ui.ac.id/login")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testuser")  
        password_input.send_keys("testpassword")
        self.browser.find_element(by=By.NAME, value="submit").click()


        login_button = self.browser.find_element(By.CLASS_NAME, "login_btn")
        login_button.click()
        
        # Now go to the homepage
        self.browser.get("http://catherine-aurellia-mental-health-tracker.pbp.cs.ui.ac.id")

        element: WebElement = self.browser.find_element(by=By.TAG_NAME, value="h1")

        self.assertEqual("Mental Health Tracker", element.text)

    def test_page_title_is_correct(self):
        self.browser.get("http://localhost:8000")

        self.assertEqual("PBD Mental Health Tracker", self.browser.title)