# -- coding: utf-8 --
import time
import datetime
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from links import *
from edit_trades import *
from buttons import *
from change_status import *
import json
import requests
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #self.date_trade = self.define_date()

        # Chromedriver

    def setUp(self):
        ser = Service('chromedriver.exe')
        op = webdriver.ChromeOptions()
        self.cd = webdriver.Chrome(service=ser, options=op)

    def Open_Login_Page(self, driver):
        driver.get("https://stage.www.vtbconnect.ru/login")

    def Login(self, driver, email, password):
        self.assertIn(u"Авторизация", driver.title)
        elem = driver.find_elements(By.CSS_SELECTOR, '[type="text"][class="ant-input ant-input-lg"]')
        elem[0].send_keys(email)
        elem1 = driver.find_element(By.CSS_SELECTOR, '[type="password"][class="ant-input ant-input-lg"]')
        elem1.send_keys(password)
        driver.find_element(By.CSS_SELECTOR, '[type="submit"][class*="ant-btn Login__form-button"]').click()
        time.sleep(3)
        print('login OK')

    def test_create_trade1(self):
        # Запуск Chromedriver
        driver = self.cd
        _links = Links
        _buttons = Buttons
        _edit_trades = Edit_trades
        _change_status = Change_status
        _trade_links = {}

        # Открытие страницы авторизации
        self.Open_Login_Page(driver)

        # Авторизация под glazovaft@yandex.ru
        self.Login(driver, email='glazovaft@yandex.ru', password='Password123#')
        driver.get("https://stage.www.vtbconnect.ru/trade/3612")
        time.sleep(2)
        _buttons.edit_trade(self, driver)
        driver.find_element(By.XPATH, '/htm11l/body/div[1]/div/div/div/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[3]/div[1]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[3]/div[1]').click()
        time.sleep(5)
        _buttons.save_changes(self, driver)
        #_edit_trades.edit_specs(self, driver)
        #_buttons.save_changes(self, driver)
        time.sleep(3)

    #def test_search_in_python_org(self):
        #current_time = datetime.datetime.now()
        #times = current_time.minute+65
        #if times >= 60:
            #times -= 60
        #print(times)

    #def test_current_date (self):
        #current_date = datetime.datetime.now()
        #day = current_date.day
        #month = current_date.month
        #month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                      #'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

        #year = current_date.year
        #date_start = str(day) + " " + month_list[month-1] + " " + str(year) + " г."
        #date_title = '[title={_date}]'.format(_date=date_start)
        #print(date_title)

        #current_time = datetime.datetime.now()
        #hours = current_time.hour+1
        #times = current_time.minute + 5
        #if times >= 60:
            #times -= 60
        #hour_start = '/html/body/div[3]/div/div/div/div[2]/div[1]/ul/li[{_hours}]'.format(_hours = hours)
        #minute_start = '/html/body/div[3]/div/div/div/div[2]/div[2]/ul/li[{_minutes}]'.format(_minutes = times)
        #print(hour_start)
        #print(minute_start)

    #def test_fail_path(self):
        #current_dir = os.path.dirname(r'C:\Users\Saya\Desktop\specifications_form_3шт.xls')  # получаем путь к директории текущего исполняемого файла
        #file_path = os.path.join(current_dir, "specifications_form_3шт.xls")  # добавляем к этому пути имя файла
        #spec1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[1]/span/div/span/div/div/button').click()
        #spec1.send_keys(r'C:\Users\Saya\Desktop\specifications_form_3шт.xls')
        #pyautogui.click(file_path)
        #print(file_path)

    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()

