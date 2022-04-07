import configparser
import time

import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
import subprocess

from webdriver_manager.chrome import ChromeDriverManager

from emum.Property import Property

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browserName", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    config = configparser.RawConfigParser()
    config.read(Property.report_environment_path.value)
    browser_name = request.config.getoption("browserName")
    if browser_name == config.get('details', 'chromeBrowser'):
        #driver = webdriver.Chrome(executable_path= Property.chrome_driver_path.value)
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == config.get('details', 'firefoxBrowser'):
        driver = webdriver.Firefox(executable_path= Property.firefox_driver_path.value)
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(Property.url.value)
    driver.maximize_window()
    request.cls.driver = driver
    yield  # Run all other pytest_runtest_makereport non wrapped hooks
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(3)
    driver.quit()

    # @pytest.mark.hookwrapper
    # @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    # def pytest_runtest_makereport(item):
    # All code prior to yield statement would be ran prior
    # to any other of the same fixtures defined

    # outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks
    # report = outcome.get_result()

    # if report.when == 'call' or report.when == "setup":
    # xfail = hasattr(report, 'wasxfail')
    # if (report.skipped and xfail) or (report.failed and not xfail):
    # file_name = report.nodeid.replace("::", "_") + ".png"
    # _capture_screenshot(file_name)

    # def _capture_screenshot(name):
    # driver.get_screenshot_as_file(name)
