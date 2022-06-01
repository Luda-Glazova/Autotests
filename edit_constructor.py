import time
import datetime
import unittest
from trade_constructor import *
from buttons import *
from links import *
from datetime import datetime
import pyautogui
import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class Edit_constructor(object):

    # Подтверждение котнатктного лица
    def edit_contact(self, driver):
        Contact1 = driver.find_element(By.CSS_SELECTOR, '[value="Нарек"]')
        Contact1.send_keys(u'\ue009' + u'\ue003')
        Contact1.send_keys("Нарек")
        time.sleep(3)
        Contact1.send_keys(Keys.RETURN)

    # Удаление второго и третьего адресов
    def delete_additional_addresses(self, driver):
        Town2_delete = driver.find_element(By.CSS_SELECTOR,
                                    'div#root div:nth-child(12) > div > div > div > span > div > input')
        Town2_delete.send_keys(u'\ue009' + u'\ue003')
        Town3_delete = driver.find_element(By.CSS_SELECTOR,
                                    'div#root div:nth-child(13) > div > div > div > span > div > input')
        Town3_delete.send_keys(u'\ue009' + u'\ue003')

    # Удаление второй и третьей спецификации
    def delete_edit_spec(self, driver):
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'div:nth-child(4) > div > svg').click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div > svg').click()
        time.sleep(2)

    # Добавление нового адреса при редактировании
    def add_addres(self, driver):
        driver.find_element(By.CSS_SELECTOR, 'div#root div:nth-child(12) > a').click()
        Town2_2 = driver.find_element(By.CSS_SELECTOR,
                                      'div#root div:nth-child(12) > div > div > div > span > div > input')
        Town2_2.send_keys("г Псков")
        time.sleep(3)
        Town2_2.send_keys(Keys.RETURN)
        time.sleep(5)

    # Копирование спецификации (нажатие кнопки "Сделать копию")
    def edit_copy_spec(self, driver):
        driver.find_element(By.CSS_SELECTOR, '.button:nth-child(1)').click()

    # Добавление и заполнение третьей спецификации и заполнение ее вручную---------------------------------------------------------------------------
    def edit_third_spec(self, driver):
        # Добавление третьей спецификации (кнопка Добавить)
        # driver.find_element(By.CSS_SELECTOR, '.button:nth-child(1)').click() (Создание копии первой спеки, если это необходимо)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, '.button:nth-child(2)').click()

        # Заполнение поля: "Количество"
        time.sleep(2)
        Count3_3 = driver.find_element(By.XPATH, '//div[4]/div[2]/div/div[2]/div/div/div/span/div/input')
        Count3_3.send_keys("5")

        # Заполнение поля: "Наименование"
        Name3_3 = driver.find_element(By.XPATH, '//div[4]/div[2]/div[2]/div/div/div/span/div/textarea')
        Name3_3.send_keys("Отредактирован")

        # Заполнение поля: "Описание"
        Description3_3 = driver.find_element(By.XPATH, '//div[4]/div[2]/div[3]/div/div/div/span/div/textarea')
        Description3_3.send_keys("Отредактирован")
        time.sleep(7)

        # ОКПД
        driver.find_element(By.CSS_SELECTOR,
                            "div#root div:nth-child(4) > div.form > div:nth-child(4) > div > div > div > span > div > div > div > span").click()
        time.sleep(7)
        OKPD3_3 = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div[4]/div/div/div/span/div/div/div/div/div/div/div/div/input")

        OKPD3_3.click()
        OKPD3_3.send_keys("22.29.25.000")
        time.sleep(3)
        OKPD3_3.send_keys(Keys.RETURN)

        # Заполнение поля: "Цена за единицу"
        Count3_3 = driver.find_element(By.XPATH, '//div[4]/div[2]/div[5]/div/div/div/div/span/div/input')
        Count3_3.send_keys("100")

        # Заполнение поля: "Единица измерения"
        driver.find_element(By.CSS_SELECTOR,
                            "div#root div:nth-child(4) > div.form > div:nth-child(5) > div:nth-child(2) > div > div > div > span > div > span").click()
        time.sleep(3)
        UNIT3_3 = driver.find_element(By.XPATH,
                                      "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div[5]/div[2]/div/div/div/span/div/div/div/div/div/div/input")
        time.sleep(1)
        UNIT3_3.send_keys('Штука')
        time.sleep(1)
        UNIT3_3.send_keys(Keys.ARROW_DOWN)
        UNIT3_3.send_keys(Keys.RETURN)

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------