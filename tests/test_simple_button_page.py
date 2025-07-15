from selenium.webdriver.common.by import By
from pages.simple_button_page import SimpleButtonPage

def test_button1_exist(browser):
    simple_button_page = SimpleButtonPage(browser)
    simple_button_page.open()
    assert simple_button_page.button_is_displayed()

def test_button1_clicked(browser):
    simple_button_page = SimpleButtonPage(browser)
    simple_button_page.open()
    simple_button_page.click_button()
    assert 'Submitted' == simple_button_page.result_text()
