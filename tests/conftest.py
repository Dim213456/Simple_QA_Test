import pytest
from selenium import webdriver

@pytest.fixture()
def browser(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    return wd




