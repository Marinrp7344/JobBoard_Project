from django.test import TestCase

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class Hosttest(LiveServerTestCase):
    def testhomepage(self):


        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))        
        driver.get('http://127.0.0.1:8000/')
       
        # implemented so selenium has time to setup browser
        time.sleep(5)

        title = driver.title
        print(title)

        driver.close()
        driver.quit()

class buttonClicktest(LiveServerTestCase):
    def testhomepage(self):


        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))        
        driver.get('http://127.0.0.1:8000/')
       
        # needed so that selenium has time to setup browser
        time.sleep(5)

        # select the view button of the first object  
        view_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/a")
        view_button.click()

        driver.close()
        driver.quit()