import os
import pytest
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="session")
def driver():
    """
    Creates a WebDriver once per test session.
    - Default browser: Chrome (set BROWSER=firefox to use Firefox)
    - Headless ON by default (set HEADLESS=0 to see the browser)
    """
    browser = os.getenv("BROWSER", "chrome").lower()
    headless = os.getenv("HEADLESS", "1") in ("1", "true", "yes")

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        drv = Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
    else:
        options = ChromeOptions()
        if headless:
            # modern headless mode
            options.add_argument("--headless=new")
        # CI-friendly flags (safe on most systems)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        drv = Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    drv.implicitly_wait(5)
    yield drv
    drv.quit()
