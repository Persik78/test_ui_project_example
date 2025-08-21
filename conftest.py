import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=2560,1440")

@pytest.fixture(autouse=True, scope="function")
def set_up():
    print('\nStart Test', datetime.datetime.now())
    driver = webdriver.Chrome(options=chrome_options)  # options=chrome_options, service=service
    yield driver
    driver.quit()
    print('\nFinal Test', datetime.datetime.now())
