from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import sys


# A function that it’s purpose is to test our web service.
def test_scores_service():
    my_driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver')
    my_driver.get("http://192.168.1.105:30000")
    score = my_driver.find_element(By.ID, "score").text
    if 0 <= int(score) <= 1000:
        return True
    else:
        return False


# This function calls our tests function. will return -1 as an OS exit code if the tests failed and 0 if they passed.
def main_function():
    test = test_scores_service()
    if test:
        return 0
    elif test:
        return sys.exit(-1)
