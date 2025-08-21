from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):
    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)


    #Locators
    cart = '(//div[@class="app-catalog-1ts79ul-Flex--StyledFlex eyflofv0"])[4]/span'
    catalog = '//a[@data-meta-name="DesktopHeaderFixed__catalog-menu"]'


    #Getters
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))


    #Actions
    def click_cart(self):
        self.get_cart().click()
        print('Click cart')
    def click_catalog(self):
        self.get_catalog().click()
        print('Click catalog')


    #Methods
    def open_main_page(self):
        Logger.add_start_step(method='open_main_page')
        self.driver.get(self.url)
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/')
        Logger.add_end_step(url=self.driver.current_url, method='open_main_page')

    def select_cart(self):
        Logger.add_start_step(method='select_cart')
        self.click_cart()
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/order/')
        Logger.add_end_step(url=self.driver.current_url, method='select_cart')





























