# -- coding: utf-8 --

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class PythonLogin(unittest.TestCase):

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
        self.assertIn(u"ВТБ Бизнес Коннект", driver.title)
        print('login OK')
        assert "No results found." not in driver.page_source
        driver.close()

if __name__ == "__main__":
    unittest.main()