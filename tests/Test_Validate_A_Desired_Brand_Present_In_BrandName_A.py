import time

import allure
import pytest
from base.Base import Base
from hiscoPageObjects.HomePage import HomePage
from tests.conftest import driver


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.sanity
class Test_Validate_A_Desired_Brand_Present_In_BrandName_A(Base):
    brand_initial = "letter-a"
    expected_names = "Autosplice"

    def test_select_all_brand_starts_with_A(self):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.dismiss_covid_ad()
        brand_page = homepage.click_on_Brands()
        names = brand_page.retrieve_all_brands_with_name_A(self.brand_initial)
        # names = homepage.retrieve_all_brands_with_name_A(self.brand_initial)
        log.info(names)
        if self.expected_names in names:
            assert True
        else:
            assert False
