import time
from datetime import datetime

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.Base import Base


class CommonUtils():

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def mouseHover(self, *ele):
        element = self.driver.find_element(*ele)
        self.action.move_to_element(element).perform()

    def wait_for_element(self, *webelement, time_unit):
        element = WebDriverWait(self.driver, time_unit).until(
            EC.visibility_of_element_located(*webelement))
        return element


    def switch_to_iframe(self, *frame):
        web = self.driver.switch_to.frame(*frame)
        return web