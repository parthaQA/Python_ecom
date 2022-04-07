import time
from selenium.webdriver.common.by import By
from utils.CommonUtils import CommonUtils


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)

    product_title = (By.XPATH, "//div[contains(@class, 'product-title')]/h1")
    add_to_cart = (By.XPATH, "//button[contains(text(),'Add To Cart')]")
    view_cart = (By.XPATH, "//div[@id='tst_addToCartPopup']//child::a")

    def verify_page_Title(self):
        time.sleep(3)
        return self.driver.title

    def verify_product_title(self):
        product_text = self.common.wait_for_element(self.product_title, time_unit=10)
        return product_text.text

    def click_on_add_to_cart(self):
        self.common.wait_for_element(self.add_to_cart, time_unit=10).click()

    def verify_item_is_added_to_cart(self):
        self.common.wait_for_element(self.view_cart, time_unit=10).click()

