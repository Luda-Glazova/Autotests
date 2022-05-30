import tempfile

fp = tempfile.NamedTemporaryFile(delete=True)
link_prefix = "https://stage.www.vtbconnect.ru/trade/"

# Сохранение порядкового номера торга и номера торга в ТП
def save_trade_number(pos, driver):
    item = driver.current_url[-4:]
    fp.write(('{}:{}\n'.format(pos, item)).encode('utf-8'))
    fp.seek(0)
    print(fp.name)
    fp.read().decode('utf-8')

# Получение номера торга в ТП из файла
def get_trade_number(pos):
    fp.seek(0)
    for i in fp.read().decode('utf-8').split('\n'):
        if i.split(':')[0] == str(pos):
            return i.split(':')[1]

# Получение ссылки на торг
def get_trade_number_link(pos):
    fp.seek(0)
    return link_prefix + get_trade_number(pos)


class Links(object):
    def __init__(self):
        self.trade1_link = None
        self.trade2_link = None
        self.trade3_link = None
        self.trade4_link = None
        self.trade5_link = None
        self.trade6_link = None
        self.trade7_link = None
        self.trade8_link = None
        self.trade9_link = None
        self.trade10_link = None
        self.trade11_link = None
        self.trade12_link = None

    # Сохранениние ссылок на торги------------------------------------------------------------------------------------------
    def trade1_link(self, driver):
        self.trade1_link = driver.current_url
        print(self.trade1_link[-4:])

    def trade2_link(self, driver):
        self.trade2_link = driver.current_url

    def trade3_link(self, driver):
        self.trade3_link = driver.current_url

    def trade4_link(self, driver):
        self.trade4_link = driver.current_url

    def trade5_link(self, driver):
        self.trade5_link = driver.current_url

    def trade6_link(self, driver):
        self.trade6_number = driver.current_url

    def trade7_link(self, driver):
        self.trade7_number = driver.current_url

    def trade8_link(self, driver):
        self.trade8_link = driver.current_url

    def trade9_link(self, driver):
        self.trade9_link = driver.current_url

    def trade10_link(self, driver):
        self.trade10_link = driver.current_url

    def trade11_link(self, driver):
        self.trade11_link = driver.current_url

    def trade12_link(self, driver):
        self.trade12_link = driver.current_url

    # Переход на торг----------------------------------------------------------------------------------------------------
    def go_to_trade1(self, driver):
        driver.get(self.trade1_link)

    def go_to_trade2(self, driver):
        driver.get(self.trade2_link)

    def go_to_trade3(self, driver):
        driver.get(self.trade3_link)

    def go_to_trade4(self, driver):
        driver.get(self.trade4_link)

    def go_to_trade5(self, driver):
        driver.get(self.trade5_link)

    def go_to_trade6(self, driver):
        driver.get(self.trade6_link)

    def go_to_trade7(self, driver):
        driver.get(self.trade7_link)

    def go_to_trade8(self, driver):
        driver.get(self.trade8_link)

    def go_to_trade9(self, driver):
        driver.get(self.trade9_link)

    def go_to_trade10(self, driver):
        driver.get(self.trade10_link)

    def go_to_trade11(self, driver):
        driver.get(self.trade11_link)

    def go_to_trade12(self, driver):
        driver.get(self.trade12_link)
