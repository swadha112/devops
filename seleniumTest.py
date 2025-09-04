from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_google_search():
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get("http://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium")
    search_box.submit()
    assert "Selenium" in driver.page_source
    driver.quit()
