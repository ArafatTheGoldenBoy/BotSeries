from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha

load_dotenv()
sitekey = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
url = "https://www.google.com/recaptcha/api2/demo"
solver = TwoCaptcha(os.getenv("API"))


# need to install webdriver manager


def main():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(url)
    driver.implicitly_wait(50000)
    result = solver.recaptcha(sitekey, url)
    print(result["code"])

    WebDriverWait(driver, 23).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="recaptcha-anchor"]/div[1]',
            )
        )
    ).click()
    driver.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = "
        + "'"
        + result["code"]
        + "'"
    )
    driver.find_element(By.ID, "recaptcha-demo-submit").click()
    time.sleep(20)
    # driver.close()


main()
