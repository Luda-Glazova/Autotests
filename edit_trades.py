import time
import datetime
import unittest
from edit_constructor import *
from buttons import *
from links import *
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

_edit_constructor = Edit_constructor
_buttons = Buttons
_links = Links

class Edit_trades(object):

    # Удаление второго и третьего адресов
    def edit_addresses(self, driver):
        #_links.go_to_trade1(self, driver)
        driver.get(get_trade_number(4))
        _buttons.edit_trade(self, driver)
        _edit_constructor.delete_additional_addresses(self, driver)
        _edit_constructor.edit_contact(self, driver)
        _buttons.save_changes(self, driver)

    def edit_specs(self, driver):
        #_links.go_to_trade5(self, driver)
        driver.get(get_trade_number(5))
        _buttons.edit_trade(self, driver)
        _edit_constructor.delete_edit_spec(self, driver)
        _edit_constructor.delete_edit_spec(self, driver)
        _edit_constructor.edit_contact(self, driver)
        _buttons.save_changes(self, driver)