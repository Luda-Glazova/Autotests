import time
import datetime
import unittest
from edit_constructor import *
from buttons import *
from links import *
from trade_constructor import *
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

_edit_constructor = Edit_constructor
_buttons = Buttons
_links = Links
_trade_constructor = Trade_constructor

class Change_status(object):

    def change_to_publish(self, id):
        url = 'https://stage.www.vtbconnect.ru/api/rest/v2/bids/bid-qa-tools'
        payload = json.dumps({
            "bid_id": get_trade_number(id),
            "status": 1
        })
        headers = {
        'Authorization': 'token 3895a57711b5d5c70614b6e09d6cfc8d56cca9b5',
        'Content-Type': 'application/json'
        }

        response = requests.request("PATCH", url, headers=headers, data=payload)
        print(response.text)

    def change_to_choose(self, id):
        url1 = 'https://stage.www.vtbconnect.ru/api/rest/v2/bids/bid-qa-tools'
        payload1 = json.dumps({
            "bid_id": get_trade_number(id),
            "status": 0
        })
        headers1 = {
        'Authorization': 'token 3895a57711b5d5c70614b6e09d6cfc8d56cca9b5',
        'Content-Type': 'application/json'
        }

        response1 = requests.request("PATCH", url1, headers=headers1, data=payload1)
        print(response1.text)
