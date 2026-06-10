# Vanilla Python local test — verifies the BrowserStack Local tunnel.
from selenium import webdriver


def run():
    driver = webdriver.Remote(
        command_executor="https://hub.browserstack.com/wd/hub",
        options=webdriver.ChromeOptions(),
    )
    try:
        driver.get("http://bs-local.com:45454")
        assert driver.title == "BrowserStack Local", driver.title
        print("Vanilla Python local test passed.")
    finally:
        driver.quit()


if __name__ == "__main__":
    run()
