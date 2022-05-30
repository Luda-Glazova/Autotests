# -- coding: utf-8 --
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def test_login_chrome(self):
        ser = Service('../chromedriver.exe')
        op = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ser, options=op)
        driver.get("https://stage.www.vtbconnect.ru/login")
        self.assertIn(u"Авторизация", driver.title)
        elem = driver.find_elements(By.CSS_SELECTOR, '[type="text"][class="ant-input ant-input-lg"]')
        elem[0].send_keys('sp.23@mail.ru')
        elem1 = driver.find_element(By.CSS_SELECTOR, '[type="password"][class="ant-input ant-input-lg"]')
        elem1.send_keys("111")
        driver.find_element(By.CSS_SELECTOR, '[type="submit"][class*="ant-btn Login__form-button"]').click()
        time.sleep(7)
        self.assertIn(u"Публичные", driver.title)
        print('login OK')
        #driver.find_element(By.CSS_SELECTOR, '[href*="trades"][class*="border-b-0"]').click()
        #self.assertIn(u"Действующие", driver.title)
        #print('trades OK')
        #assert "No results found." not in driver.page_source
        driver.close()

    def test_trades_page(self):
        ser = Service('../chromedriver.exe')
        op = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ser, options=op)
        driver.get("https://stage.www.vtbconnect.ru/new/platform/")
        driver.find_element(By.CSS_SELECTOR, '[href*="trades"][class*="border-b-0"]').click()
        #self.assertIn(u"Запросы предложений", driver.title)
        print('trades OK')
        driver.close()

if __name__ == "__main__":
    unittest.main()


