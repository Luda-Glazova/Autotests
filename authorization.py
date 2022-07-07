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

class Authorization:
    def __init__(self):
        ser = Service('chromedriver.exe')
        op = webdriver.ChromeOptions()
        self.chromedriver = webdriver.Chrome(service=ser, options=op)

    #Логаут(деавторизация)
    def logout(self):
        self.chromedriver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.sidebar > div > div.ant-layout-sider-children > aside > a').click()
        time.sleep(2)
        self.chromedriver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/header/div/div/div[4]/button/div').click()
        time.sleep(2)
        self.chromedriver.find_element(By.CSS_SELECTOR, 'div#gatsby-focus-wrapper button[type="button"].flex.items-center.justify-center.text-n1.border-2.px-6.button-modules--container--267eH.header-modules--exitButton--2sVif.button-modules--secondary--I_OvC').click()
        time.sleep(3)

    # Открытие страницы авторизации
    def open_login_page(self):
        self.chromedriver.get("https://stage.www.vtbconnect.ru/login")


    # Авторизация
    def login(self, email, password):
        #self.assertIn(u"Авторизация", self.chromedriver.title)
        #assert u"Авторизация" in self.chromedriver.title
        elem = self.chromedriver.find_elements(By.CSS_SELECTOR, '[type="text"][class="ant-input ant-input-lg"]')
        elem[0].send_keys(email)
        elem1 = self.chromedriver.find_element(By.CSS_SELECTOR, '[type="password"][class="ant-input ant-input-lg"]')
        elem1.send_keys(password)
        self.chromedriver.find_element(By.CSS_SELECTOR, '[type="submit"][class*="ant-btn Login__form-button"]').click()
        time.sleep(3)
        print('login OK')

    # Авторизация под glazovaft5@yandex.ru, чтобы вызвать _authorization.login_ft('glazovaft5@yandex.ru', 'Password123#')
    def login_ft(self, email, password):
        self.login(email=email, password=password)