# Vanilla Python sample — no test framework. The BrowserStack SDK patches
# selenium webdriver.Remote at import time and runs this script across the
# platforms in browserstack.yml.  Run:  browserstack-sdk python bstack_sample.py
from selenium import webdriver
from selenium.webdriver.common.by import By


def run():
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=webdriver.ChromeOptions(),
    )
    try:
        driver.get("https://bstackdemo.com/")
        product = driver.find_element(By.XPATH, '//*[@id="1"]/p').text
        driver.find_element(By.XPATH, '//*[@id="1"]/div[4]').click()
        driver.find_element(By.CLASS_NAME, "float-cart__content")
        cart = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]').text
        assert cart == product, f"cart {cart!r} != product {product!r}"
        print("Vanilla Python sample passed: cart matches product.")
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
