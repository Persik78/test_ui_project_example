import datetime
from faker import Faker



class Base():

    def __init__(self, driver):
        self.driver = driver



    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    """Method assert word"""
    @staticmethod
    def assert_word(word, result):
        value_word = word.text
        assert value_word == result, print('Bad value word:', value_word, 'result:', result)
        print("Good value word:", value_word)

    """Method screenshot"""
    def get_screenshot(self, method):
        now_date = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        name_screenshot = 'screenshot_' + method + '_' + now_date + '.png'
        print(name_screenshot)
        self.driver.save_screenshot('screenshots/' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method assert total cost"""
    @staticmethod
    def assert_total_cost(total_cost, result):
        assert total_cost == result, print('Bad total cost:', total_cost, 'result:', result)
        print("Good value total cost:", total_cost)

    """Method create test name"""
    @staticmethod
    def create_test_name():
        faker = Faker('ru_RU')
        name = faker.name().split()
        return name

    """Method create test phone number"""
    @staticmethod
    def create_test_phone_number():
        faker = Faker('ru_RU')
        number = faker.phone_number()
        return number

    """Method create test street name"""
    @staticmethod
    def create_test_address():
        faker = Faker('ru_RU')
        address = faker.street_address().split(',')
        return address

    """Method create test email"""
    @staticmethod
    def create_test_email():
        faker = Faker('ru_RU')
        email = faker.email()
        return email