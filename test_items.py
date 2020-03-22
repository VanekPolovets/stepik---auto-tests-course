import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_see_add_to_cart_button(browser):
	browser.get(link)
	time.sleep(30)
	assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
   