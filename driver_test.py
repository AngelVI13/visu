from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://lichess.org/training/")
assert "Puzzles" in driver.title

elem = driver.find_element_by_class_name("title")
print(elem.text)
time.sleep(1)


def get_previous_moves(num: int):
    for i in range(num + 1):  # it starts by taking screen shot of final position
        # todo ? maybe it only needs to take a picture at the final board and the beginning board
        elem = driver.find_element_by_class_name("puzzle__board")
        elem.screenshot(f"image{i}.png")

        time.sleep(0.5)

        prev_btn = driver.find_element_by_xpath("/html/body/div[1]/main/div[3]/div/button[2]")
        prev_btn.click()

        time.sleep(0.5)


get_previous_moves(10)

driver.close()