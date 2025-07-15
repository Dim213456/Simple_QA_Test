from selenium.webdriver.common.by import By
from pages.looks_like_a_button_page import LooksLikeAButton

def test_button2_exist(browser):
    looks_like_a_button = LooksLikeAButton(browser)
    looks_like_a_button.open()
    assert looks_like_a_button.button_is_displayed()

def test_button2_clicked(browser):
    looks_like_a_button = LooksLikeAButton(browser)
    looks_like_a_button.open()
    looks_like_a_button.click_button()
    assert 'Submitted' == looks_like_a_button.result_text()