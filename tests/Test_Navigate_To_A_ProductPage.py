import time

import allure
import pytest
from base.Base import Base
from hiscoPageObjects.HomePage import HomePage
from tests.conftest import driver


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
class Test_Navigate_To_A_ProductPage(Base):
    productName = "Abrasives"
    expected_title = "Coated & Bonded Abrasives | Belts, Disks & More"

    def test_validate_user_can_navigate_to_productPage(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.dismiss_covid_ad()
        homepage.click_on_products()
        log.info(f"user clicks on {self.productName}")
        product_page = homepage.navigate_to_a_productPage(self.productName)
        actual_title = product_page.verify_page_Title()
        assert actual_title == self.expected_title
        log.info(f"{self.expected_title} is verified")
