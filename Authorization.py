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

class Authorizatoin(object):

    #Логаут(деавторизация)
    def logout(self):
        driver.find_element(By.CSS_SELECTOR, '#root > div > div > div > div.sidebar > div > div.ant-layout-sider-children > aside > a').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/header/div/div/div[4]/button/div').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'div#gatsby-focus-wrapper button[type="button"].flex.items-center.justify-center.text-n1.border-2.px-6.button-modules--container--267eH.header-modules--exitButton--2sVif.button-modules--secondary--I_OvC').click()
        time.sleep(3)

