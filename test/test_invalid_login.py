from selenium.webdriver.common.by import By

def test_invalid_login_message(driver):
    # Public demo app
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    flash = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in flash
