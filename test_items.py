import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    print("Timer for check for browser language...")
    time.sleep(30)
    add_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert add_button, "Add to basket button not founded"
