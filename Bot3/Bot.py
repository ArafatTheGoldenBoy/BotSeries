from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# need to install webdriver manager


def main():
    # proxy = "14.231.161.89:8080"  # desired proxy ip with port
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_argument("--proxy-server=%s" % proxy)
    # options.accept_insecure_certs = True
    # options.add_argument()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get("https://visa.vfsglobal.com/ind/en/deu/login")
    driver.implicitly_wait(50000)
    user = driver.find_element(By.ID, "mat-input-0")
    user.send_keys("yasinarafat3.de@gmail.com" + Keys.RETURN)
    pass2 = driver.find_element(By.ID, "mat-input-1")
    pass2.send_keys("U8vZv9NW9$5iwF!" + Keys.RETURN)
    time.sleep(5000)
    login = driver.find_element(
        By.CLASS_NAME,
        "mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted",
    ).click()

    # driver.close()


main()
