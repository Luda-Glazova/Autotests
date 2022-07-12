# -- coding: utf-8 --
import time
import datetime
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from buttons import *
import pyautogui
import pyautogui as pyautogui
from change_status import *
import json
import requests
from selenium.webdriver.common.keys import Keys

class Bets_constructor(object):
    # Ставки для торга(не забудь подождать после загрузки страницы!)

    # Заполнение поля цена в рублях (первая ставка)
    def price_bet1(self, driver):
        Price = driver.find_element(By.CSS_SELECTOR, 'input#price')
        Price.send_keys("2500")

    # Заполнение поля цена в рублях (вторая ставка)
    def price_bet2(self, driver):
        Price = driver.find_element(By.CSS_SELECTOR, 'input#price')
        Price.send_keys("2000")

    # Заполнение поля цена в рублях (первая ставка переторжка)
    def price_bet1_resell(self, driver):
        Price = driver.find_element(By.CSS_SELECTOR, 'input#price')
        Price.send_keys("1500")

    # Заполнение поля цена в рублях (вторая ставка переторжка)
    def price_bet2_resell(self, driver):
        Price = driver.find_element(By.CSS_SELECTOR, 'input#price')
        Price.send_keys("1000")

    #Заполнение поля комментарий
    def сomment_bet(self, driver):
        time.sleep(5)
        Comment = driver.find_element(By.CSS_SELECTOR, '[id=comment][name=comment]')
        Comment.send_keys("Автотест")

    # Добавление файла в ставку
    def add_file_bet(self, driver):
        time.sleep(2)
        pyautogui.write(r'C:\Users\Saya\Desktop\form.xlsx')
        time.sleep(1)
        pyautogui.press('enter')

    #Модальное окно подтверждения при первой ставке
    def modal_window_first_bet(self, driver):
        driver.find_element(By.CSS_SELECTOR, 'div#root span.ant-checkbox > input').click()
        SMS_code = driver.find_element(By.CSS_SELECTOR, 'input#sms_code')
        SMS_code.send_keys("9999")
        driver.find_element(By.CSS_SELECTOR, 'div#root div.reveal_form > button[type="button"]').click()

    # Модальное окно подтверждения при первой ставке
    def modal_window_second_bet(self, driver):
        SMS_code = driver.find_element(By.CSS_SELECTOR, 'input#sms_code')
        SMS_code.send_keys("9999")
        driver.find_element(By.CSS_SELECTOR, 'div#root div.reveal_form > button[type="button"]').click()

