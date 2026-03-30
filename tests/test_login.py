def test_login(driver):
    driver.get("https://example.com")
    assert "Example" in driver.title
