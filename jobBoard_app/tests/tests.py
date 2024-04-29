from django.test import TestCase

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class SadPostCreation(LiveServerTestCase):
    def test_post_creation_happy(self):


        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))        
        driver.get('http://127.0.0.1:8000/')
       
        # implemented so selenium has time to setup browser
        time.sleep(2)

        #go to login page
        login = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/div/a[5]")
        login.click()

        time.sleep(1)
        username = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[1]/td[2]/input")
        password = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[2]/td[2]/input")

        username.send_keys("Thunk")
        password.send_keys("Bankai7721")

        password.send_keys(webdriver.Keys.ENTER)
        
        time.sleep(1)

        createButton = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/div/a[3]")
        createButton.click()

        time.sleep(2)

        
        title = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[1]/td/input")
        about = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[2]/td/input")
        desc = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[3]/td/textarea")
        pay = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[5]/td/input")
        visible = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[6]/td/input")

        title.send_keys("Test")
        about.send_keys("Test")
        desc.send_keys("Test")
        pay.send_keys("$300")
        visible.click()

        

        submit = driver.find_element(By.XPATH, "/html/body/div/div/form/input[2]")
        submit.click()
        time.sleep(2)

        driver.close()
        driver.quit()

class HappyPostCreation(LiveServerTestCase):
    def test_post_creation_sad(self):
        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))        
        driver.get('http://127.0.0.1:8000/')
       
        # implemented so selenium has time to setup browser
        time.sleep(2)

        #go to login page
        login = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/div/a[5]")
        login.click()

        time.sleep(1)
        username = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[1]/td[2]/input")
        password = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[2]/td[2]/input")

        username.send_keys("Thunk")
        password.send_keys("Bankai7721")

        password.send_keys(webdriver.Keys.ENTER)
        
        time.sleep(1)

        createButton = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/div/a[3]")
        createButton.click()

        time.sleep(1)
        
        title = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[1]/td/input")
        about = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[2]/td/input")
        desc = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[3]/td/textarea")
        pay = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[5]/td/input")
        visible = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[6]/td/input")

        about.send_keys("Test")
        desc.send_keys("Test")
        pay.send_keys("$300")
        visible.click()

        submit = driver.find_element(By.XPATH, "/html/body/div/div/form/input[2]")
        submit.click()
        time.sleep(3)

        driver.close()
        driver.quit()

class HappyDelete(LiveServerTestCase):
    def test_post_creation_sad(self):
        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))        
        driver.get('http://127.0.0.1:8000/')
       
        # implemented so selenium has time to setup browser
        time.sleep(2)

        #go to login page
        login = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/div/a[5]")
        login.click()

        time.sleep(1)
        username = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[1]/td[2]/input")
        password = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[2]/td[2]/input")

        username.send_keys("Thunk")
        password.send_keys("Bankai7721")

        password.send_keys(webdriver.Keys.ENTER)
        
        time.sleep(1)

        viewButton = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/div/a[2]")
        viewButton.click()

        time.sleep(1)
        
        delete = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/a[3]")
        delete.click()

        time.sleep(1)

        driver.close()
        driver.quit()

class SadDelete(LiveServerTestCase):
    def test_post_creation_sad(self):
        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))        
        driver.get('http://127.0.0.1:8000/')
       
        # implemented so selenium has time to setup browser
        time.sleep(2)

        #go to login page
        login = driver.find_element(By.XPATH, "/html/body/div/nav/div/div/div/a[5]")
        login.click()

        time.sleep(2)
        username = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[1]/td[2]/input")
        password = driver.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[2]/td[2]/input")

        username.send_keys("Gulp")
        password.send_keys("Bankai7721")

        password.send_keys(webdriver.Keys.ENTER)
        
        time.sleep(2)

        driver.get('http://127.0.0.1:8000/posts/7/delete_post/')

        time.sleep(2)

        driver.close()
        driver.quit()