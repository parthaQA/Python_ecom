from enum import Enum


class Property(Enum):
    report_environment_path = "../reports/environment.properties"
    chrome_driver_path = "../resource/chromedriver.exe"
    firefox_driver_path = "../resource/geckodriver.exe"
    url = "https://www.hisco.com/"


