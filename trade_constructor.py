import time
import datetime
import unittest
from datetime import datetime

import pyautogui as pyautogui
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.keys import Keys


# Определяем сегодняшний день
def define_date():
    #current_date = datetime.datetime.now()
    current_date = datetime.now()
    day = current_date.day
    if day < 10:
        day = f"0{day}"
    month = current_date.month
    if month < 10:
        month = f"0{month}"
    year = current_date.year
    return f"{day}.{month}.{year}"

class Trade_constructor(object):

    # Нейминг торгов--------------------------------------------------------------------------------------------------------
    # Заполнение поля: "Наименование закупки/продажи"
    # Записываемм дату
    def __init__(self, *args, **kwargs):
        super(Trade_constructor).__init__(*args, **kwargs)
        self.date_trade = self.define_date()

    # Заполняем данными поле "Наименование закупки/продажи"
    def trade_1(self, driver, _date_trade):
        name = f"Выкатка {_date_trade} (Аукцион, Со снижением НМЦ, без ставки и без победителя)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.send_keys(name)

    def trade_2(self, driver, _date_trade):
        name2 = f"Выкатка {_date_trade} (Аукцион, Без снижения НМЦ, со ставкой и без победителя)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name2)

    def trade_3(self, driver, _date_trade):
        name3 = f"Выкатка {_date_trade} (Аукцион, Без указания НМЦ, со ставкой, будет отменен)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name3)

    def trade_4(self, driver, _date_trade):
        name4 = f"Выкатка {_date_trade} (Аукцион, Со снижением НМЦ, есть ставка, есть победитель)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name4)

    def trade_5(self, driver, _date_trade):
        name5 = f"Выкатка {_date_trade} (Аукцион, Со снижением НМЦ, открытая переторжка)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name5)

    def trade_6(self, driver, _date_trade):
        name6 = f"Выкатка {_date_trade} (Аукцион, Без снижением НМЦ, закрытая переторжка)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name6)

    def trade_7(self, driver, _date_trade):
        name7 = f"Выкатка {_date_trade} (Закрытый, Со снижением НМЦ, без ставки и без победителя)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.send_keys(name7)

    def trade_8(self, driver, _date_trade):
        name8 = f"Выкатка {_date_trade} (Закрытый, Без снижения НМЦ, со ставкой и без победителя)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name8)

    def trade_9(self, driver, _date_trade):
        name9 = f"Выкатка {_date_trade} (Закрытый, Без указания НМЦ, со ставкой, будет отменен)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name9)

    def trade_10(self, driver, _date_trade):
        name10 = f"Выкатка {_date_trade} (Закрытый, Со снижением НМЦ, есть ставка, есть победитель)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name10)

    def trade_11(self, driver, _date_trade):
        name11 = f"Выкатка {_date_trade} (Закрытый, Со снижением НМЦ, открытая переторжка)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name11)

    def trade_12(self, driver, _date_trade):
        name12 = f"Выкатка {_date_trade} (Закрытый, Без снижением НМЦ, закрытая переторжка)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.clear()
        naimenovanie.send_keys(name12)

    #-------------------------------------------------------------------------------------------------------------------
    # Общая информация-заполняется одинаково для всех торгов
    # Заполнение поля: "Общая информация"
    def common_info(self, driver):
        Info = driver.find_element(By.CSS_SELECTOR, '[id=description]')
        Info.send_keys("Автотест")

    # Заполнение поля: "Внутренняя категория из списка"
    def inner_category(self, driver):
        driver.find_element(By.CSS_SELECTOR,
                            'div#root div:nth-child(5) > div > div > div > span > div > div > div > span.floating-input-label__placeholder').click()
        driver.find_element(By.XPATH, '//*[@id="rc-tree-select-list_1"]/ul/li[2]/span[2]/span').click()
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > div > div > div.page-main-layout-content.is-auth.ant-layout').click()

    # Заполнение поля: "Начальная цена"
    def start_price(self, driver):
        Price = driver.find_element(By.CSS_SELECTOR, '[id=nmck]')
        Price.send_keys("3000")

    # Заполнение поля: "Контактное лицо"
    def contact(self, driver):
        Contact = driver.find_element(By.CSS_SELECTOR, '[placeholder*="Контактное"]')
        Contact.send_keys("Нарек")
        time.sleep(3)
        Contact.send_keys(Keys.RETURN)

    # Заполнение поля: "Контактный телефон"
    def phone(self, driver):
        Phone = driver.find_element(By.CSS_SELECTOR, '[id=contact_phone]')
        Phone.send_keys("123")

    # Заполнение поля: "Условия поставки и оплаты"
    def delivery(self, driver):
        Delivery = driver.find_element(By.CSS_SELECTOR, '[id=payment_terms]')
        Delivery.send_keys("123")
        time.sleep(3)

    # Заполнение поля: "Адреса/места хранения и поставки"
    def town(self, driver):
        Town = driver.find_element(By.CSS_SELECTOR, '[placeholder*="Адрес"]')
        Town.send_keys("г Саратов")
        time.sleep(3)
        Town.send_keys(Keys.RETURN)

    # Заполнение поля: "Дата старта торга"(устанавливаем дату-сегодня)
    def date_start(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[id=date_start]').click()
        driver.find_element(By.CSS_SELECTOR, 'div.ant-calendar-footer > span > a').click()

    # Заполнение поля: "Дата завершения торга"(устанавливаем дату-сегодня)
    def date_end(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[id=date_end]').click()
        driver.find_element(By.CSS_SELECTOR, 'div.ant-calendar-footer > span > a').click()

    # Заполнение спецификации
    # Заполнение поля: "Количество"
    def count_spec(self, driver):
        Count = driver.find_element(By.CSS_SELECTOR, '[id=items-1-amount]')
        Count.send_keys("10")

    # Заполнение поля: "Наименование"
    def name_spec(self, driver):
        Name = driver.find_element(By.CSS_SELECTOR, '[id=items-1-name]')
        Name.send_keys("Автотест")

    # Заполнение поля: "Описание"
    def description_spec(self, driver):
        Description = driver.find_element(By.CSS_SELECTOR, '[id=items-1-description]')
        Description.send_keys("Автотест")
        time.sleep(7)

    # ОКПД
    def okpd_spec(self, driver):
        driver.find_element(By.CSS_SELECTOR,
                            ".form_input:nth-child(4) .ant-spin-nested-loading .floating-input-label__placeholder").click()
        time.sleep(7)
        OKPD = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/div[4]/div/div/div/span/div/div/div/div/div/div/div/div/input")
        OKPD.send_keys("41.10.10.000")
        time.sleep(3)
        OKPD.send_keys(Keys.RETURN)

    # Заполнение поля: "Цена за единицу"
    def price_spec(self, driver):
        Price_spec = driver.find_element(By.CSS_SELECTOR, '[id=items-1-cost]')
        Price_spec.send_keys("300")

    # Заполнение поля: "Единица измерения"
    def shtuka_spec(self, driver):
        driver.find_element(By.CSS_SELECTOR,
                            ".form_row:nth-child(5) > .form_input:nth-child(2) .floating-input-label__placeholder").click()
        time.sleep(3)
        UNIT = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/div[5]/div[2]/div/div/div/span/div/div/div/div/div/div/input")
        time.sleep(1)
        UNIT.send_keys('Штука')
        time.sleep(1)
        UNIT.send_keys(Keys.ARROW_DOWN)
        UNIT.send_keys(Keys.RETURN)

    # ----------------------------------------------------------------------------------------------------------------------
    # Выбор типа аукцион(для закрытого ничего не делаем)
    def choose_type_auction(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[id=auction_type]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/ul/li[2]').click()

    def so_snigeniem_nmc(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[title*=Без]').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[1]').click()

    # Выбор вида без снижения НМЦ
    def bez_snigenia_nmc(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[title*=Со]').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[2]').click()

    # Выбор вида без указания НМЦ
    def bez_ukazania_nmc(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[title*=Без]').click()
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div/ul/li[3]').click()

    # Смена валюты на Доллар
    def USD(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[title*=Росс]').click()
        time.sleep(3)
        USD = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div[6]/div[2]/div/div/div/span/div/div/div/div/div/div/div[2]/div/input')
        USD.send_keys("Доллар США")

    # Смена валюты на Евро
    def EUR(self, driver):
        driver.find_element(By.CSS_SELECTOR, '[title*=Росс]').click()
        time.sleep(3)
        EUR = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div[6]/div[2]/div/div/div/span/div/div/div/div/div/div/div[2]/div/input')
        EUR.send_keys("Евро")

    # Загрузка спецификации(3шт)
    def spec_download(self, driver):
        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[1]/span/div/span/div/div/button').click()
        time.sleep(5)
        pyautogui.click(x=411, y=424)  # Вписываем имя файла в строку "Имя файла"
        pyautogui.write(r'C:\Users\Saya\Desktop\specifications_form_3st.xls')
        pyautogui.click(x=716, y=458)  # Кнопка открыть
        time.sleep(5)

    # Добавление 2х дополнительных адресов
    def additional_addresses(self, driver):
        driver.find_element(By.CSS_SELECTOR, 'div#root div:nth-child(12) > a').click()
        Town2 = driver.find_element(By.CSS_SELECTOR,
                                    'div#root div:nth-child(12) > div > div > div > span > div > input')
        Town2.send_keys("г Уфа")
        time.sleep(3)
        Town2.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.find_element(By.CSS_SELECTOR, 'div#root div:nth-child(13) > a').click()
        Town3 = driver.find_element(By.CSS_SELECTOR,
                                    'div#root div:nth-child(13) > div > div > div > span > div > input')
        Town3.send_keys("г Пермь")
        time.sleep(3)
        Town3.send_keys(Keys.RETURN)
        time.sleep(5)

    # Копирование спецификации (нажатие кнопки "Сделать копию")
    def copy_spec(self, driver):
        driver.find_element(By.CSS_SELECTOR, '.button:nth-child(1)').click()

    # Добавление и заполнение третьей спецификации и заполнение ее вручную---------------------------------------------------------------------------
    def trird_spec(self, driver):
        # Добавление третьей спецификации (кнопка Добавить)
        # driver.find_element(By.CSS_SELECTOR, '.button:nth-child(1)').click() (Создание копии первой спеки, если это необходимо)
        driver.find_element(By.CSS_SELECTOR, '.button:nth-child(2)').click()

        # Заполнение поля: "Количество"
        Count3 = driver.find_element(By.CSS_SELECTOR, '[id=items-3-amount]')
        Count3.send_keys("10")

        # Заполнение поля: "Наименование"
        Name3 = driver.find_element(By.CSS_SELECTOR, '[id=items-3-name]')
        Name3.send_keys("Автотест")

        # Заполнение поля: "Описание"
        Description3 = driver.find_element(By.CSS_SELECTOR, '[id=items-3-description]')
        Description3.send_keys("Автотест")
        time.sleep(7)

        # ОКПД
        driver.find_element(By.CSS_SELECTOR,
                            "#items-3-okpd > div > div").click()
        time.sleep(7)
        OKPD3 = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div[4]/div/div/div/span/div/div/div/div/div/div/div/div/input")
        OKPD3.send_keys("23.13.13.130")
        time.sleep(3)
        OKPD3.send_keys(Keys.RETURN)

        # Заполнение поля: "Цена за единицу"
        Count3 = driver.find_element(By.CSS_SELECTOR, '[id=items-3-cost]')
        Count3.send_keys("300")

        # Заполнение поля: "Единица измерения"
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div[5]/div[2]/div/div/div/span/div").click()
        time.sleep(3)
        UNIT3 = driver.find_element(By.XPATH,
                                    "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[4]/div[2]/div[5]/div[2]/div/div/div/span/div/div/div/div/div/div/input")
        time.sleep(1)
        UNIT3.send_keys('Штука')
        time.sleep(1)
        UNIT3.send_keys(Keys.ARROW_DOWN)
        UNIT3.send_keys(Keys.RETURN)

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # Добавление файлов(требование к предмету закупки и форма КП)
    def add_docs(self, driver):
        driver.find_element(By.CSS_SELECTOR, '.form_file:nth-child(1) .ant-btn:nth-child(2)').click()
        time.sleep(5)
        pyautogui.click(x=411, y=424)  # Вписываем имя файла в строку "Имя файла"
        pyautogui.write(r'C:\Users\Saya\Desktop\specifications_form_3st.xls')
        pyautogui.click(x=716, y=458)  # Кнопка открыть
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, '.form_file:nth-child(2) .ant-btn:nth-child(2)').click()
        time.sleep(5)
        pyautogui.click(x=411, y=424)  # Вписываем имя файла в строку "Имя файла"
        pyautogui.write(r'C:\Users\Saya\Desktop\specifications_form_3st.xls')
        pyautogui.click(x=716, y=458)  # Кнопка открыть
        time.sleep(3)

# if __name__ == "__Main__":
# unittest.main()
