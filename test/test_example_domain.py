def test_example_domain_title(driver):
    driver.get("https://example.com/")
    assert "Example Domain" in driver.title
