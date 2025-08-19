import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=2560,1440")
service = Service("/opt/chromedriver/chromedriver-linux64/chromedriver")

@pytest.fixture(autouse=True, scope="function")
def set_up():
    print('Start Test', datetime.datetime.now())
    driver = webdriver.Chrome(options=chrome_options, service=service)  # options=chrome_options, service=service
    yield driver
    driver.quit()
    print('Final Test', datetime.datetime.now())