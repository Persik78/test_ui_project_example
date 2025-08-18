import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

from utilities.logger import Logger


class CatalogMenu(Base):
    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    # Locators Main

    main_word_in_catalog = '/html/body/div/div/div/div/div/div/div[3]/h4'
    main_word_in_item = '/html/body/div/div/div/div/div/div/div[4]/a/h4'

    # Locators Item
    general_path_to_catalog_item = '/html/body/div/div/div/div/div/div/div[5]/div/div/div/div/div[1]/div/div[1]/div'
    pc_components = general_path_to_catalog_item + '/a[1]/div/span'
    laptop_and_desktop = general_path_to_catalog_item + '/a[2]/div/span'
    smartphones_and_tablets = general_path_to_catalog_item + '/a[3]/div/span'

    # Locators Column items
    general_path_column = '(//div[@class="app-catalog-ywlc2u-Column--Column ebado1d0"])'
    first_column = general_path_column + '[1]'
    second_column = general_path_column + '[2]'
    third_column = general_path_column + '[3]'

    # Locators Sub column items
    first_sub_column = first_column + '/div[1]'
    second_sub_column = second_column + '/div[2]'
    third_sub_column = third_column + '/div[3]'

    # Locators Title Sub column items
    title_first_sub_column = first_sub_column + '/a/span'
    title_second_sub_column = second_sub_column + '/a/span'
    title_third_sub_column = third_sub_column + '/a/span'


    # Getters
    # Getters Main

    def get_main_word_in_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_in_catalog)))
    def get_main_word_in_item(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_in_item)))

    # Getters Item
    def get_pc_components(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pc_components)))
    def get_laptop_and_desktop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_and_desktop)))
    def get_smartphones_and_tablets(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_and_tablets)))

    # Getters Column items
    def get_first_column(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_column)))
    def get_second_column(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.second_column)))
    def get_third_column(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.third_column)))

    # Getters Title Sub column items
    def get_title_first_sub_column(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_first_sub_column)))
    def get_title_second_sub_column(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_second_sub_column)))
    def get_title_third_sub_column(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_third_sub_column)))


    # Actions
    # Actions clicks

    def click_pc_components(self):
        self.get_pc_components().click()
        print('Click PC components')
    def click_laptop_and_desktop(self):
        self.get_laptop_and_desktop().click()
        print('Click Laptop and Desktop')
    def click_title_first_sub_column(self):
        self.get_title_first_sub_column().click()
        print('Click Title first sub column')
    def click_title_second_sub_column(self):
        self.get_title_second_sub_column().click()
        print('Click Title second sub column')
    def click_title_third_sub_column(self):
        self.get_title_third_sub_column().click()
        print('Click Title third sub column')

    #Actions move to element
    def move_to_pc_components(self):
        ActionChains(self.driver).move_to_element(self.get_pc_components()).perform()
    def move_laptop_and_desktop(self):
        ActionChains(self.driver).move_to_element(self.get_laptop_and_desktop()).perform()
    def move_smartphones_and_tablets(self):
        ActionChains(self.driver).move_to_element(self.get_smartphones_and_tablets()).perform()


    #Methods

    def open_catalog_processor(self):
        Logger.add_start_step(method='open_catalog_processor')
        self.assert_word(self.get_main_word_in_catalog(), 'Каталог')
        self.move_to_pc_components()
        self.assert_word(self.get_main_word_in_item(), 'Комплектующие для ПК')
        self.click_title_first_sub_column()
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/catalog/processory/?ref=mainmenu')
        Logger.add_end_step(url=self.driver.current_url, method='open_catalog_processor')
