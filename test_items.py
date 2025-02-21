# В файл test_items.py напишите тест, который проверяет, что страница товара на сайте 
# содержит кнопку добавления в корзину. Например, можно проверять товар, 
# доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

import pytest
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket(browser):
    browser.get(link)    
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Кнопка добавления в корзину не найдена!"
