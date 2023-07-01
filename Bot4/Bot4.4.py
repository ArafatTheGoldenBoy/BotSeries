# system libraries
import os
import random
import time

# selenium libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# recaptcha libraries
import speech_recognition as sr

# import ffmpy
import requests
import urllib

# import pydub


url = "https://www.google.com/recaptcha/api2/demo"


def main():
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--start-maximized")
    options.add_argument(
        "user-data-dir=C:\\Users\\Yasin.DESKTOP-RVLJ0DB\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    )
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    time.sleep(5)
    driver.get(url)
    time.sleep(5)
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(
            (
                By.CSS_SELECTOR,
                "iframe[src^='https://www.google.com/recaptcha/api2/anchor']",
            )
        )
    )
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "span#recaptcha-anchor"))
    ).click()
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it(
            (
                By.CSS_SELECTOR,
                "iframe[title='recaptcha challenge expires in two minutes']",
            )
        )
    )
    WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))
    ).click()
    driver.switch_to.default_content()
    time.sleep(5)
    driver.find_element(By.ID, "//*[@id=':2']").click()
    src = driver.find_element(By.ID, "//*[@id='rc-audio']/div[7]/a").get_attribute(
        "src"
    )
    print(src)


main()
