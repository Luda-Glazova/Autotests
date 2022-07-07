# -- coding: utf-8 --
import time
import datetime
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from links import *
from authorization import *
from edit_trades import *
from buttons import *
from change_status import *
import json
import requests
from selenium.webdriver.common.keys import Keys

class Bets(object):
    # Ставки для торга(не забудь подождать после загрузки страницы!)

    #Первая ставка для аукциона(без вложения файла)
    def first_bet_auction_with_price(self, driver):
        Comment = driver.find_element(By.CSS_SELECTOR, '[id=comment][name=comment]')
        Comment.send_keys("Автотест")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '.button_max-height_45').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, 'div#root span.ant-checkbox > input').click()
        SMS_code = driver.find_element(By.CSS_SELECTOR, 'input#sms_code')
        SMS_code.send_keys("9999")
        driver.find_element(By.CSS_SELECTOR, 'div#root div.reveal_form > button[type="button"]').click()