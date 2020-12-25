link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import time


class ButtonNotFound(Exception):
    pass


def test_find_add_to_cart_button(browser):
    browser.get(link)
    try:
        # time.sleep(30)
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket').text
        assert len(button) > 0, 'Кнопка не найдена'
    except exceptions.NoSuchElementException:
        raise ButtonNotFound('Элемент отсутствует на странице')
