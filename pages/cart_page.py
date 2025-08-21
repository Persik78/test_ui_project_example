from utilities.logger import Logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)



    # Locators
    main_word_cart_page = '//div[@class="css-1l3z4gj-Flex--StyledFlex eyflofv0"]/span'
    button_back_main_menu = '//div[@class="css-1l3z4gj-Flex--StyledFlex eyflofv0"]/a/span'
    button_make_order = '//button[@class="e11203e30 css-fi4v85-Button--StyledButton-Button--Button ekx3zbi0"]'
    button_continue_guest = '//button[@class="e11203e30 css-10hmcp9-Button--StyledButton-Button--Button ekx3zbi0"]/span'


    # Getters
    def get_main_word_cart_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_cart_page)))
    def get_button_back_main_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_back_main_menu)))
    def get_button_make_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_make_order)))
    def get_button_continue_guest(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue_guest)))


    # Actions
    def click_button_back_main_menu(self):
        self.get_button_back_main_menu().click()
        print('Click button back main menu')
    def click_button_make_order(self):
        self.get_button_make_order().click()
        print('Click button make order')
    def click_button_continue_guest(self):
        self.get_button_continue_guest().click()
        print('Click button continue guest')


    # Methods
    def select_button_back_main_menu(self):
        Logger.add_start_step(method='select_button_back_main_menu')
        self.click_button_back_main_menu()
        self.assert_url('https://www.citilink.ru/')
        Logger.add_end_step(url=self.driver.current_url, method='select_button_back_main_menu')

    def select_button_make_order_unauthorized(self):
        Logger.add_start_step(method='select_button_make_order_unauthorized')
        self.click_button_make_order()
        self.click_button_continue_guest()
        self.assert_url('https://www.citilink.ru/order/checkout/')
        Logger.add_end_step(url=self.driver.current_url, method='select_button_make_order_unauthorized')













