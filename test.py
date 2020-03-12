import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  
import time
import unittest
class Test_(unittest.TestCase):
		def test_abs1(self):
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)
			input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
			input1.send_keys("Ivan")
			input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
			input2.send_keys("Petrov")
			input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
			input3.send_keys("Smolensk")
			button = browser.find_element_by_css_selector("button.btn")
			button.click()
			self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 1')
			time.sleep(10)
			browser.quit()
		def test_abs2(self):
			link = "http://suninjuly.github.io/registration2.html"
			browser = webdriver.Chrome()
			browser.get(link)
			input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[1]/input")
			input1.send_keys("Ivan")
			input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
			input2.send_keys("Ivan")
			button = browser.find_element_by_css_selector("button.btn")
			button.click()
			self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 2')
			time.sleep(10)
			browser.quit()
if __name__ == "__main__":
	unittest.main()

    