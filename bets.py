# -- coding: utf-8 --
import time
import datetime
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from buttons import *
from bets_constructor import *
import json
import requests
from selenium.webdriver.common.keys import Keys

_bets_constructor = Bets_constructor
_buttons = Buttons

class Bets(object):

    # Ставки для торга(не забудь подождать после загрузки страницы!)

    # Первая ставка для аукциона(без вложения файла НЕ ДЛЯ ТИПА БЕЗ УКАЗАНИЯ НМЦ)
    def first_bet_auction_without_price(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _buttons.make_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)

    # Первая ставка для аукциона(с файлом КП НЕ ДЛЯ ТИПА БЕЗ УКАЗАНИЯ НМЦ)
    def first_bet_auction_without_price_with_file(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _buttons.load_kp(self, driver)
        _bets_constructor.add_file_before_bet(self, driver)
        _buttons.make_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)

    # Вторая ставка для аукциона(без вложения файла)
    def second_bet_auction_without_price(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _buttons.make_bet(self, driver)
        _buttons.cancel_first_bet(self, driver)
        _bets_constructor.modal_window_second_bet(self, driver)

    # Первая ставка универсальная(цена,коммент и файл, КРОМЕ ПРОЦЕНТНЫХ СТАВОК)
    def first_bet_for_all(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet1(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)

    # Вторая ставка универсальная(цена,коммент и файл, КРОМЕ ПРОЦЕНТНЫХ СТАВОК и переторжки)
    def second_bet_for_all(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet2(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _buttons.cancel_first_bet(self, driver)
        _bets_constructor.modal_window_second_bet(self, driver)

    # Первая ставка универсальная для переторжки(цена,коммент и файл, КРОМЕ ПРОЦЕНТНЫХ СТАВОК)
    def first_bet_for_resell(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet1_resell(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _buttons.cancel_first_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)

    # Вторая ставка универсальная для переторжки(цена,коммент и файл, КРОМЕ ПРОЦЕНТНЫХ СТАВОК)
    def second_bet_for_resell(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet2_resell(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _buttons.cancel_first_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)

    # Первая ставка процентная(процент,коммент и файл)
    def first_bet_for_all_persent(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet1_persent(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)

    # Вторая ставка процентная(процент,коммент и файл)
    def second_bet_for_all_persent(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet2_persent(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _buttons.cancel_first_bet(self, driver)
        _bets_constructor.modal_window_second_bet(self, driver)

    # Первая ставка процентная для переторжки(процент,коммент и файл)
    def first_bet_for_resell_persent(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet1_persent_resell(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _buttons.cancel_first_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)

    # Вторая ставка процентная для переторжки(процент,коммент и файл)
    def second_bet_for_resell_persent(self, driver):
        _bets_constructor.сomment_bet(self, driver)
        _bets_constructor.price_bet2_persent_resell(self, driver)
        _buttons.load_kp_before_bet(self, driver)
        _bets_constructor.add_file_bet(self, driver)
        _buttons.make_bet(self, driver)
        _buttons.cancel_first_bet(self, driver)
        _bets_constructor.modal_window_first_bet(self, driver)