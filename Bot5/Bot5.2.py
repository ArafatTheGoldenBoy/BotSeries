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
sitekey = "6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI"
url = "https://visa.vfsglobal.com/ind/en/deu/login"
solver = TwoCaptcha(os.getenv("API"))


def main():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[contains(.,'Accept All Cookies')]").click()
    driver.implicitly_wait(50000)
    user = driver.find_element(By.ID, "mat-input-0")
    user.send_keys(os.getenv("EMAIL"))
    pass2 = driver.find_element(By.ID, "mat-input-1")
    pass2.send_keys(os.getenv("PASSWORD"))
    time.sleep(2)
    result = solver.recaptcha(sitekey, url)
    print(result)
    time.sleep(4)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//div[@class="row custom-card"]//a')
            )
        )
        a = driver.find_elements(By.XPATH, '//div[@class="row custom-card"]//a')
        a = a[1]
        time.sleep(2.5)
        a.click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//a[@class="lets-get-started"]')
            )
        )
        a = driver.find_element(By.XPATH, '//a[@class="lets-get-started"]')
        time.sleep(4.5)
        a.click()

    except:
        print("Iframe not opened")
        driver.quit()


main()
