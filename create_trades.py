# -- coding: utf-8 --
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


class PythonOrgSearch(unittest.TestCase):


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
        _trade_constructor = Trade_constructor
        _buttons = Buttons
        _links = Links
        _date = define_date()

        # Открытие страницы авторизации
        self.Open_Login_Page(driver)

        # Авторизация под glazovaft@yandex.ru
        self.Login(driver, email='glazovaft@yandex.ru', password='Password123#')

        # Переход на страницу "Запросы"
        driver.find_element(By.CSS_SELECTOR, '[href*="trades"][class*="border-b-0"]').click()
        time.sleep(3)

        # Нажатие кнопки "Создать"
        driver.find_element(By.CSS_SELECTOR, '[type=button][class*=ant-btn]').click()
        time.sleep(3)

        #Первый торг(создан с нуля, аукцион, со снижением НМЦ, не аккредитованный, без ставок и без победителя)--------------------------------------
        _trade_constructor.choose_type_auction(self, driver)
        _trade_constructor.trade_1(self, driver, _date)
        _trade_constructor.common_info(self, driver)
        _trade_constructor.inner_category(self, driver)
        _trade_constructor.start_price(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.phone(self, driver)
        _trade_constructor.delivery(self, driver)
        _trade_constructor.town(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _trade_constructor.count_spec(self, driver)
        _trade_constructor.name_spec(self, driver)
        _trade_constructor.description_spec(self, driver)
        _trade_constructor.okpd_spec(self, driver)
        _trade_constructor.price_spec(self, driver)
        _trade_constructor.shtuka_spec(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(1, driver)

        # Второй торг(размещен повторно, аукцион, без снижения НМЦ, не аккредитованный,валюта Доллар, со ставкой без победителя)
        _buttons.re_create(self, driver)
        _trade_constructor.bez_snigenia_nmc(self, driver)
        _trade_constructor.trade_2(self, driver, _date)
        _trade_constructor.USD(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(2, driver)

        # Третий торг(размещен повторно, аукцион, Без указания НМЦ, не аккредитованный,загружено несколько спецификаций через шаблон, со ставкой, будет отменен)
        _buttons.re_create(self, driver)
        _trade_constructor.bez_ukazania_nmc(self, driver)
        _trade_constructor.trade_3(self, driver, _date)
        _trade_constructor.spec_download(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(3, driver)

        # Четвертый торг(размещен повторно, аукцион, со снижением НМЦ, не аккредитованный,несколько адресов, есть ставка, есть победитель)
        _buttons.re_create(self, driver)
        _trade_constructor.so_snigeniem_nmc(self, driver)
        _trade_constructor.trade_4(self, driver, _date)
        _trade_constructor.contact(self, driver)
        _trade_constructor.additional_addresses(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(4, driver)

        # Пятый торг(размещен повторно, аукцион, со снижением НМЦ, не аккредитованный,несколько спецификаций(добавлены вручную), открытая переторжка)
        _buttons.re_create(self, driver)
        _trade_constructor.trade_5(self, driver, _date)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _trade_constructor.copy_spec(self, driver)
        _trade_constructor.Third_spec(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(5, driver)

        # Шестой торг(размещен повторно, аукцион, со снижением НМЦ, не аккредитованный,прикреплены документы при создании в : Требования к предмету закупки и Форма коммерческого предложения, закрытая переторжка)
        _buttons.re_create(self, driver)
        _trade_constructor.trade_6(self, driver, _date)
        _trade_constructor.add_docs(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(6, driver)

        #Седьмой торг(создан с нуля, закрытый, со снижением НМЦ, не аккредитованный, без ставок и без победителя)--------------------------------------
        driver.find_element(By.CSS_SELECTOR, 'li:nth-child(3) > a > span').click()
        driver.find_element(By.CSS_SELECTOR, '[type=button][class*=ant-btn]').click()
        _trade_constructor.trade_7(self, driver, _date)
        _trade_constructor.common_info(self, driver)
        _trade_constructor.inner_category(self, driver)
        _trade_constructor.start_price(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.phone(self, driver)
        _trade_constructor.delivery(self, driver)
        _trade_constructor.town(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _trade_constructor.count_spec(self, driver)
        _trade_constructor.name_spec(self, driver)
        _trade_constructor.description_spec(self, driver)
        _trade_constructor.okpd_spec(self, driver)
        _trade_constructor.price_spec(self, driver)
        _trade_constructor.shtuka_spec(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(7, driver)

        # Восьмой торг(размещен повторно, закрытый, без снижения НМЦ, не аккредитованный,валюта Доллар, со ставкой без победителя)
        _buttons.re_create(self, driver)
        _trade_constructor.bez_snigenia_nmc(self, driver)
        _trade_constructor.trade_8(self, driver, _date)
        _trade_constructor.USD(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(8, driver)

        # Девятый торг(размещен повторно, закрытый, Без указания НМЦ, не аккредитованный,загружено несколько спецификаций через шаблон, со ставкой, будет отменен)
        _buttons.re_create(self, driver)
        _trade_constructor.bez_ukazania_nmc(self, driver)
        _trade_constructor.trade_9(self, driver, _date)
        _trade_constructor.spec_download(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(9, driver)

        # Десятый торг(размещен повторно, закрытый, со снижением НМЦ, не аккредитованный,несколько адресов, есть ставка, есть победитель)
        _buttons.re_create(self, driver)
        _trade_constructor.so_snigeniem_nmc(self, driver)
        _trade_constructor.trade_10(self, driver, _date)
        _trade_constructor.contact(self, driver)
        _trade_constructor.additional_addresses(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(10, driver)

        # Одиннадцатый торг(размещен повторно, закрытый, со снижением НМЦ, не аккредитованный,несколько спецификаций(добавлены вручную), открытая переторжка)
        _buttons.re_create(self, driver)
        _trade_constructor.trade_11(self, driver, _date)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _trade_constructor.copy_spec(self, driver)
        _trade_constructor.Third_spec(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(11, driver)

        # Двенадцатый торг(размещен повторно, закрытый, со снижением НМЦ, не аккредитованный,прикреплены документы при создании в : Требования к предмету закупки и Форма коммерческого предложения, закрытая переторжка)
        _buttons.re_create(self, driver)
        _trade_constructor.trade_12(self, driver, _date)
        _trade_constructor.add_docs(self, driver)
        _trade_constructor.contact(self, driver)
        _trade_constructor.date_start(self, driver)
        _trade_constructor.date_end(self, driver)
        _buttons.publish(self, driver)
        save_trade_number(12, driver)

        time.sleep(15)
        # Заполнение торга данными
        # Выбор типа:Аукцион
        driver.find_element(By.CSS_SELECTOR, '[id=auction_type]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/ul/li[2]').click()

        # Заполнение поля: "Наименование закупки/продажи"
        current_date = datetime.datetime.now()
        day = current_date.day
        if day < 10:
            day = "0" + str(day)
        month = current_date.month
        if month < 10:
            month = "0" + str(month)
        year = current_date.year
        name = "Выкатка " + str(day) + "." + str(month) + "." + str(year) + "(Аукцион, Со снижением НМЦ, без ставок и без победителя)"
        naimenovanie = driver.find_element(By.CSS_SELECTOR, '[id=name]')
        naimenovanie.send_keys(name)

        # Заполнение поля: "Общая информация"
        Info = driver.find_element(By.CSS_SELECTOR, '[id=description]')
        Info.send_keys("Автотест")

        # Заполнение поля: "Внутренняя категория из списка"
        driver.find_element(By.CSS_SELECTOR,
                            'div#root div:nth-child(5) > div > div > div > span > div > div > div > span.floating-input-label__placeholder').click()
        driver.find_element(By.XPATH, '//*[@id="rc-tree-select-list_1"]/ul/li[2]/span[2]/span').click()
        driver.find_element(By.CSS_SELECTOR,
                            '#root > div > div > div > div.page-main-layout-content.is-auth.ant-layout').click()

        # Заполнение поля: "Начальная цена"
        Price = driver.find_element(By.CSS_SELECTOR, '[id=nmck]')
        Price.send_keys("3000")

        # Заполнение поля: "Контактное лицо"
        Contact = driver.find_element(By.CSS_SELECTOR, '[placeholder*="Контактное"]')
        Contact.send_keys("Нарек")
        time.sleep(3)
        Contact.send_keys(Keys.RETURN)

        # Заполнение поля: "Контактный телефон"
        Phone = driver.find_element(By.CSS_SELECTOR, '[id=contact_phone]')
        Phone.send_keys("123")

        # Заполнение поля: "Условия поставки и оплаты"
        Delivery = driver.find_element(By.CSS_SELECTOR, '[id=payment_terms]')
        Delivery.send_keys("123")
        time.sleep(3)

        # Заполнение поля: "Адреса/места хранения и поставки"
        Town = driver.find_element(By.CSS_SELECTOR, '[placeholder*="Адрес"]')
        Town.send_keys("г Саратов")
        time.sleep(3)
        Town.send_keys(Keys.RETURN)

        # Заполнение поля: "Дата старта торга"(устанавливаем дату-сегодня)
        driver.find_element(By.CSS_SELECTOR, '[id=date_start]').click()
        driver.find_element(By.CSS_SELECTOR, 'div.ant-calendar-footer > span > a').click()
        # time.sleep(7)

        # Заполнение поля: "Время старта торга"
        # Вычисляем время и ставим время старта текущее время+5 минут
        # current_time = datetime.datetime.now()
        # hours = current_time.hour
        # times = current_time.minute + 5
        # if times >= 60:
        # times -= 60
        # Нажимаем на само поле времени
        # driver.find_element(By.CSS_SELECTOR, '[id=time_start]').click()

        # Заполняем час старта
        # hour_start = '/html/body/div[3]/div/div/div/div[2]/div[1]/ul/li[{_hours}]'.format(_hours = hours)
        # driver.find_element(By.XPATH, hour_start).click()
        # driver.find_element(By.CSS_SELECTOR, '.ant-time-picker-panel-select-option-selected:nth-child(13)').click()
        # time.sleep(7)
        # Заполняем минуту старта
        # driver.find_element(By.CSS_SELECTOR, 'ant-time-picker-panel-select-active li:nth-child(7)').click()
        # minute_start = '/html/body/div[3]/div/div/div/div[2]/div[2]/ul/li[{_minutes}]'.format(_minutes = times)
        # driver.find_element(By.XPATH, minute_start).click()

        # Заполнение поля: "Дата завершения торга"(устанавливаем дату-сегодня)
        driver.find_element(By.CSS_SELECTOR, '[id=date_end]').click()
        driver.find_element(By.CSS_SELECTOR, 'div.ant-calendar-footer > span > a').click()
        # time.sleep(7)

        # Заполнение поля: "Время завершения торга"
        # current_time = datetime.datetime.now()
        # times = current_time.minute + 15
        # if times >= 60:
        # times -= 60

        # Заполнение спецификации
        # Заполнение поля: "Количество"
        Count = driver.find_element(By.CSS_SELECTOR, '[id=items-1-amount]')
        Count.send_keys("10")

        # Заполнение поля: "Наименование"
        Name = driver.find_element(By.CSS_SELECTOR, '[id=items-1-name]')
        Name.send_keys("Автотест Торг1")

        # Заполнение поля: "Описание"
        Description = driver.find_element(By.CSS_SELECTOR, '[id=items-1-description]')
        Description.send_keys("Автотест Торг1")
        time.sleep(7)

        # ОКПД
        driver.find_element(By.CSS_SELECTOR,
                            ".form_input:nth-child(4) .ant-spin-nested-loading .floating-input-label__placeholder").click()
        time.sleep(7)
        OKPD = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div/div[2]/div[2]/div/div/div/form/div[1]/div[2]/div/div[2]/div[2]/div[4]/div/div/div/span/div/div/div/div/div/div/div/div/input")
        OKPD.send_keys("41")

        # Заполнение поля: "Цена за единицу"
        Count = driver.find_element(By.CSS_SELECTOR, '[id=items-1-cost]')
        Count.send_keys("300")

        # Заполнение поля: "Единица измерения"
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

        # Опубликовать
        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/div/form/div[2]/div[1]/div/button').click()
        time.sleep(10)

    # Выход из Chromedriver
    def tearDown(self):
        self.cd.quit()


if __name__ == "__Main__":
    unittest.main()
