import time

from selenium import webdriver
from Libss.amazon import Amazon

booksToAdd = ["Experiences of Test Automation: Case Studies of Software Test Automation",
              "Agile Testing: A Practical Guide for Testers and Agile Teams",
              "Selenium WebDriver 3 Practical Guide: End-to-end automation testing for web and mobile browsers "
              "with Selenium WebDriver, 2nd Edition"]

driver = webdriver.Chrome()

amazon = Amazon(driver)
amazon.go_to("https://www.amazon.com/")
amazon.sign_in("pass", "username")
amazon.add_to_cart_paperback(booksToAdd)
amazon.open_cart()
amazon.save_for_later("Experiences of Test Automation")
amazon.delete_from_cart("Agile Testing")
amazon.change_quantity("Selenium WebDriver 3 Practical Guide", 3)
amazon.gift("Selenium WebDriver 3 Practical Guide")
amazon.change_quantity("Selenium WebDriver 3 Practical Guide", 1)