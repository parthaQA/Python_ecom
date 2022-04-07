import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
#from seleniumpagefactory.Pagefactory import PageFactory

from hiscoPageObjects.BrandPage import BrandPage
from hiscoPageObjects.ProductPage import ProductPage
from utils.CommonUtils import CommonUtils


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)


    product = (By.XPATH, "//a[text()='Products']")
    brand = (By.XPATH, "//a[text()='Brands']")
    search = (By.XPATH, "//li[@id = 'wideSearch']//child::input")
    covid_frame = (By.NAME, "ju_iframe_553670")


    def click_on_products(self):
        self.common.mouseHover(*HomePage.product)

    def navigate_to_a_productPage(self, productName):
        product_name = self.driver.find_element_by_xpath("//a[text()='" + productName + "']")
        product_name.click()
        return ProductPage(self.driver)

    def click_on_Brands(self):
        self.common.wait_for_element(self.brand, time_unit=2).click()
        return BrandPage(self.driver)

    def search_a_product(self, product_name):
        self.common.wait_for_element(self.search, time_unit=2).send_keys(product_name)
        xpath = "//div[@class= 'shortDescription']/strong"
        time.sleep(4)
        search_product = self.driver.find_element_by_xpath(xpath)
        if product_name in search_product.text:
            search_product.click()

    def dismiss_covid_ad(self):
        frame_name = "ju_iframe_553670"
        if self.common.wait_for_element(self.covid_frame, time_unit=15).is_displayed():
            self.driver.switch_to.frame(frame_name)
            close_button = self.driver.find_element_by_xpath("//span[text()='x']")
            close_button.click()
            self.driver.switch_to.default_content()
        else:
            print("no iframe is available")