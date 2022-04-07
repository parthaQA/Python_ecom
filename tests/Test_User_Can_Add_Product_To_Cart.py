import allure
import pytest

from base.Base import Base
from hiscoPageObjects.HomePage import HomePage
from hiscoPageObjects.ProductPage import ProductPage
from utils.CommonUtils import CommonUtils


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sanity
class Test_User_Can_Add_Product_To_Cart(Base):

    expected_prod_name = "Isopropyl"
    expected_title = "Isopropyl Alcohol (IPA) 70% IPA, 1 Gallon (For Use In Manufacturing Processes)"

    def test_user_can_add_product_to_cart(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.dismiss_covid_ad()
        productpage = ProductPage(self.driver)
        homepage.search_a_product(self.expected_prod_name)
        actual_text = productpage.verify_product_title()
        if self.expected_prod_name in actual_text:
            log.info(f"you have opened the right page: {self.expected_prod_name}")
            assert True
        else:
            log.info(f"you are in wrong product page: {actual_text}")
            assert False
        productpage.click_on_add_to_cart()
        productpage.verify_item_is_added_to_cart()
        assert actual_text == self.expected_title

