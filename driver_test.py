from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://lichess.org/training/")
assert "Puzzles" in driver.title

elem = driver.find_element_by_class_name("puzzle__board")
elem.screenshot("test.png")

driver.close()