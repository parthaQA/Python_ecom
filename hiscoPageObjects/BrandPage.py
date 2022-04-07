from selenium.webdriver.common.by import By

from utils.CommonUtils import CommonUtils


class BrandPage:

    def __init__(self, driver):
        self.driver = driver
        self.common = CommonUtils(self.driver)


    def retrieve_all_brands_with_name_A(self, brand_a):
        name = (By.XPATH, "//div[@id='" + brand_a + "']//following-sibling::div")
        names = self.common.wait_for_element(name, time_unit=10)
        return names.text