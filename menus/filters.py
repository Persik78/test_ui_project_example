import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver.common.action_chains import ActionChains

from utilities.logger import Logger


class Filters(Base):
    def __init__(self, driver):
        super().__init__(driver)


    # Locators
    filters_menu = '//div[@data-meta-name="FiltersLayout"]'
    apply_filters = '//button[@class="e133q3zd0 app-catalog-1j7df12-Button--StyledButton-Button--Button ekx3zbi0"]'

    # Locators filters processor
    # Locators Brand processor
    brand_amd = '//input[@id="amd"]'

    # Locators Series processor
    series_ryzen_7 = '//input[@id="156_26ryzend17"]'

    # Locators Socket processor
    socket_am5 = '//input[@id="157_26am5"]'

    # Locators Generation processor
    generation_ryzen_7000 = '//input[@id="24524_26amdd1ryzend17xxx"]'



    # Getter
    def get_filters_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filters_menu)))
    def get_apply_filters(self):
        # return self.driver.find_element(By.XPATH, self.apply_filters)
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply_filters)))

    # Getter filters processor
    # Getter Brand processor
    def get_brand_processor_amd(self):
        return self.driver.find_element(By.XPATH, self.brand_amd)

    # Getter Series processor
    def get_series_ryzen_7(self):
        return self.driver.find_element(By.XPATH, self.series_ryzen_7)

    # Getter Socket processor
    def get_socket_am5(self):
        return self.driver.find_element(By.XPATH, self.socket_am5)

    # Getter Generation processor
    def get_generation_ryzen_7000(self):
        return self.driver.find_element(By.XPATH, self.generation_ryzen_7000)



    # Actions
    def move_filters_menu(self):
        ActionChains(self.driver).move_to_element(self.get_filters_menu()).perform()
    def click_apply_filters(self):
        self.driver.execute_script("arguments[0].click();", self.get_apply_filters())



    # Methods
    def select_apply_filters(self):
        Logger.add_start_step(method='select_apply_filters')
        self.click_apply_filters()
        time.sleep(5) # URL не успевает измениться
        self.get_current_url()
        self.assert_url('https://www.citilink.ru/catalog/processory/?ref=mainmenu&pf=rating.any%2Cdiscount.any&f=rating.any%2Cdiscount.any%2Camd%2C156_26ryzend17%2C157_26am5%2C24524_26amdd1ryzend17xxx')
        Logger.add_end_step(url=self.driver.current_url, method='select_apply_filters')

    # Methods filters processor
    def select_brand_processor_amd(self):
        Logger.add_start_step(method='select_brand_processor_amd')
        ActionChains(self.driver).move_to_element(self.get_brand_processor_amd()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_brand_processor_amd())
        print('Select filter brand processor AMD')
        Logger.add_end_step(url=self.driver.current_url, method='select_brand_processor_amd')
    def select_series_ryzen_7(self):
        Logger.add_start_step(method='select_series_ryzen_7')
        ActionChains(self.driver).move_to_element(self.get_series_ryzen_7()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_series_ryzen_7())
        print('Select filter series ryzen 7 processor')
        Logger.add_end_step(url=self.driver.current_url, method='select_series_ryzen_7')
    def select_socket_am5(self):
        Logger.add_start_step(method='select_socket_am5')
        ActionChains(self.driver).move_to_element(self.get_socket_am5()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_socket_am5())
        print('Select filter socket AM5 processor')
        Logger.add_end_step(url=self.driver.current_url, method='select_socket_am5')
    def select_generation_ryzen_7000(self):
        Logger.add_start_step(method='select_generation_ryzen_7000')
        ActionChains(self.driver).move_to_element(self.get_generation_ryzen_7000()).perform()
        self.driver.execute_script("arguments[0].click();", self.get_generation_ryzen_7000())
        print('Select filter generation ryzen 7000 processor')
        Logger.add_end_step(url=self.driver.current_url, method='select_generation_ryzen_7000')










