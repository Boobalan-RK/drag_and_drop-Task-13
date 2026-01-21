import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to initialize and quit Chrome browser
    """

    # Disable SSL verification for webdriver-manager (works in v4+)
    os.environ['WDM_SSL_VERIFY'] = '0'

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    service = Service(
        ChromeDriverManager().install()
    )

    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
