from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Chrome_driver:

    def __init__(self):
        ser = Service('../chromedriver.exe')
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


    def Exit_driver(self):
        self.cd.quit()