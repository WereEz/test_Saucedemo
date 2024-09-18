"""
Модуль для тестирования https://www.saucedemo.com/
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def init_driver():
    """
    Инициализирует WebDriver для браузера Chrome с заданными параметрами.
    :return driver: Экземпляр WebDriver
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    return driver



def test_purchase():
    """
    Тестирует авторизацию на сайте, выбор товара, оформление покупки и 
    проверяет успешное завершение покупки.
    """
    driver = init_driver()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory.html" in driver.current_url, "Login failed"

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "shopping_cart_container").click()
        cart_item = driver.find_element(
            By.CLASS_NAME, "inventory_item_name").text
        assert cart_item == "Sauce Labs Backpack", "Product is not in the cart"

        driver.find_element(By.ID, "checkout").click()
        driver.find_element(By.ID, "first-name").send_keys("a")
        driver.find_element(By.ID, "last-name").send_keys("b")
        driver.find_element(By.ID, "postal-code").send_keys("1")
        driver.find_element(By.ID, "continue").click()
        driver.find_element(By.ID, "finish").click()

        complete_header = driver.find_element(
            By.CLASS_NAME, "complete-header").text
        assert complete_header, "Purchase was not successful"

        print("Test Passed: Purchase completed successfully.")

    except Exception as e:
        print(f"Test Failed: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_purchase()
