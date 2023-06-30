from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_recaptcha_solver import RecaptchaSolver
import time
import os
from dotenv import load_dotenv

load_dotenv()
sitekey = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
url = "https://www.google.com/recaptcha/api2/demo"


# need to install webdriver manager


def main():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(url)
    solve = RecaptchaSolver(driver)
    time.sleep(3)
    iframe = driver.find_element(
        By.XPATH,
        '//*[@id="recaptcha-demo"]/div/div/iframe',
    )
    solve.click_recaptcha_v2(iframe)
    # solve.solve_recaptcha_v2_challenge(iframe)
    time.sleep(20)
    driver.find_element(By.ID, "recaptcha-demo-submit").click()

    # driver.close()


main()
