import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from base.base_class import Base
from menus.filters import Filters
from pages.cart_page import CartPage
from pages.main_page import MainPage
from menus.catalog_menu import CatalogMenu
from pages.order_page import OrderPage
from pages.products_page import ProductPage

chrome_options = Options()
chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
service = Service("/opt/chromedriver/chromedriver-linux64/chromedriver")

@allure.epic('Tests buy product')
class TestBuyProduct():

    @allure.description('test buy processor amd ryzen 7 7700')
    def test_buy_processor_amd_ryzen_7_7700(self, set_up):
        driver = set_up
        main = MainPage(driver)
        main.open_main_page()
        main.click_catalog()
        catalog = CatalogMenu(driver)
        catalog.open_catalog_processor()
        time.sleep(1) # Фильтры чем то перекрыты, не получалось через явное ожидание и обычный клик по чек боксу. У меня всегда успевали фильтры подгружаться, добавил на всякий случай
        filters = Filters(driver)
        filters.move_filters_menu()
        filters.select_brand_processor_amd()
        filters.select_series_ryzen_7()
        filters.select_socket_am5()
        filters.select_generation_ryzen_7000()
        filters.select_apply_filters()

        product = ProductPage(driver)
        Base.assert_word(product.get_main_word_page(), 'Процессоры')
        product.select_add_cart_product_1()
        Base.assert_word(product.get_check_product_in_modal_window(), 'Процессор AMD Ryzen 7 7700, AM5, OEM [100-000000592]')
        product.click_buton_close_modal_window()

        main.select_cart()

        cart = CartPage(driver)
        cart.select_button_make_order_unauthorized()

        order = OrderPage(driver)
        order.entry_receipt_and_payment_delivery()

        order.move_place_an_order() #Не стал нажимать на кнопку чтобы не создался заказ

