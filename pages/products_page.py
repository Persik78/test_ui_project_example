from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)



    # Locators
    general_patch_to_product = '(//div[@class="app-catalog-1benfua-StyledWrapper e181eg3x0"])'
    main_word_page = '(//div[@class="app-catalog-o5rr6c e15ji6eo0"])/h1/div/div'

    # Locators modal window
    modal_window_before_add_cart = '//div[@class="app-catalog-c5c7vg-StyledLayout e1qwi0fy0"]'
    buton_close_modal_window = modal_window_before_add_cart + '/button'
    modal_window_text = modal_window_before_add_cart + '/div[1]/span'
    check_product_in_modal_window = modal_window_before_add_cart + '/div[3]/div/div[2]/div[2]'

    # Locators Product
    product_1 = general_patch_to_product + '[1]'

    # Locators Price product
    price_product_1 = product_1 + '//span[@data-meta-is-total="notTotal"]/span[1]'

    # Locators Product add cart
    add_cart_product_1 = product_1 + '/div[8]/div[3]/div/button'


    # Getters
    def get_main_word_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_page)))
    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))

    # Getters add cart
    def get_add_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_product_1)))

    # Getters modal window
    def get_buton_close_modal_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buton_close_modal_window)))
    def get_modal_window_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.modal_window_text)))
    def get_check_product_in_modal_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_product_in_modal_window)))


    # Actions
    # Actions clicks
    def click_add_cart_product_1(self):
        self.get_add_cart_product_1().click()
        print('Click add cart first product')
    def click_buton_close_modal_window(self):
        self.get_buton_close_modal_window().click()
        print('Click button close modal window before add cart')


    # Methods
    def select_add_cart_product_1(self):
        Logger.add_start_step(method='select_add_cart_product_1')
        self.click_add_cart_product_1()
        self.assert_word(self.get_modal_window_text(), 'Товар добавлен в корзину')
        self.get_screenshot('select_add_cart_product_1')
        Logger.add_end_step(url=self.driver.current_url, method='select_add_cart_product_1')




