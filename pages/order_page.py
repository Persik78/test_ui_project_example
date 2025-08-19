import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

from utilities.logger import Logger


class OrderPage(Base):

    # Locators
    recipients_details = '//div[@class="e1sk2tkw0 css-17j0ir3-StyledGrid--StyledGrid-composeBreakpointsStyles--arrayOfStylesByBreakpoints-Grid--WrappedGrid-Wrapper--StyledWrapper efysbo20"]'
    first_name = recipients_details + '//input[@name="firstName"]'
    last_name = recipients_details + '//input[@name="lastName"]'
    phone_number = recipients_details + '//input[@name="phone"]'
    pickup = '//div[@class="css-qdvesi e588gsg0"]/div/label[1]'
    delivery = '//div[@class="css-qdvesi e588gsg0"]/div/label[2]'
    email = '//input[@name="email"]'

    street = '//input[@name="street"]'
    add_street = '//div[@class="eqw7fo10 css-7asl3q-SelectListOption--StyledSelectListOption-SelectListOption--StyledSelectListOptionComponent e9d6jv80"]'
    building = '//input[@name="courier-delivery-new-address-form_house"]'
    price_delivery = '//*[@id="__next"]/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/label/div[2]/div/div[2]/span[1]'
    total_cost_order = '//div[@class="css-0 e1dmrhay0"]/div/div/span[2]/span/span[1]'

    place_an_order = '//button[@class="e1mb8yuw0 css-6wqf91-Button--StyledButton-Button--Button ekx3zbi0"]/span'



    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))
    def get_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pickup)))
    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))
    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))
    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))
    def get_add_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_street)))
    def get_building(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.building)))
    def get_price_delivery(self):
        return WebDriverWait(self.driver, 1200).until(EC.presence_of_element_located((By.XPATH, self.price_delivery)))
    def get_total_cost_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_cost_order)))
    def get_place_an_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_cost_order)))



    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name:', first_name)
    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name:', last_name)
    def input_phone_number(self, phone_number):
        self.get_phone_number().send_keys(phone_number)
        print('Input phone number:', phone_number)
    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input email:', email)
    def input_street(self, street):
        self.get_street().send_keys(street)
        print('Input street:', street)
    def input_building(self, building):
        self.get_building().send_keys(building)
        print('Input building:', building)

    def click_pickup(self):
        self.get_pickup().click()
        print('Click pickup')
    def click_delivery(self):
        self.get_delivery().click()
        print('Click delivery')
    def click_add_street(self):
        self.get_add_street().click()
        print('Click add street')

    def int_price_delivery(self):
        return int(self.get_price_delivery().text.replace(' ', ''))
    def int_total_cost_order(self):
        return int(self.get_total_cost_order().text.replace(' ', ''))

    def move_place_an_order(self):
        ActionChains(self.driver).move_to_element(self.get_place_an_order()).perform()
        print('Available place an order')





    # Methods
    def entry_receipt_and_payment_delivery(self):
        Logger.add_start_step(method='entry_receipt_and_payment_delivery')
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/order/checkout/')
        name = Base.create_test_name()
        self.input_first_name(name[1])
        self.input_last_name(name[0])
        self.input_phone_number(Base.create_test_phone_number())
        self.click_delivery()
        address = Base.create_test_address()
        self.input_street(address[0])
        self.click_add_street()
        self.input_building(address[1])
        self.input_email(Base.create_test_email())
        self.get_screenshot('entry_receipt_and_payment_delivery')
        self.assert_total_cost(self.int_total_cost_order() + self.int_price_delivery(), 20990 + self.int_price_delivery()) # Не получилось сделать иначе, в элементе с ценой доставки она всегда прописана, но к итоговой сумме применяется с нормальной такой задержкой (при автотесте)
        Logger.add_end_step(url=self.driver.current_url, method='entry_receipt_and_payment_delivery')
