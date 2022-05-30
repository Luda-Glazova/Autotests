import time
import unittest
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class Buttons(object):
    # Опубликовать
    def publish(self, driver):
        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div/button').click()
        time.sleep(3)

    # Разместить повторно
    def re_create(self, driver):
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '.button:nth-child(3)').click()
        time.sleep(2)

    # Редактировать
    def edit_trade(self, driver):
        driver.find_element(By.XPATH, '//div/div/button').click()

    # Сохранить
    def save_changes(self, driver):
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/form/div[2]/div[1]/div/button').click()
        time.sleep(3)