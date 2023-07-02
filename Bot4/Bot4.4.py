# system libraries
import os
import random
import time
import requests

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
from selenium_stealth import stealth
import undetected_chromedriver as uc

# recaptcha libraries
import urllib
from pydub import AudioSegment
import speech_recognition as sr
import ffmpy

url = "https://www.google.com/recaptcha/api2/demo"


def main():
    options = Options()

    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--start-maximized")

    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_argument(
        "user-data-dir=C:\\Users\\Yasin.DESKTOP-RVLJ0DB\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    )
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    )
    # just some options passing in to skip annoying popups
    options.add_argument("--no-first-run --no-service-autorun --password-store=basic")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )

    time.sleep(random.randint(3, 5))
    driver.get(url)
    driver.implicitly_wait(10)

    driver.refresh()
    driver.implicitly_wait(10)

    time.sleep(6)
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
    time.sleep(random.randint(3, 5))
    driver.switch_to.default_content()
    time.sleep(random.randint(3, 5))
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
    time.sleep(random.randint(3, 5))
    WebDriverWait(driver, 20).until(
        EC.frame_to_be_available_and_switch_to_it(
            (
                By.CSS_SELECTOR,
                "iframe[title='recaptcha challenge expires in two minutes']",
            )
        )
    )

    src = driver.find_element(By.ID, "audio-source").get_attribute("src")
    print("link:", src)
    time.sleep(random.randint(3, 5))
    urllib.request.urlretrieve(src, os.getcwd() + "\\sample.mp3")
    # convert mp3 file to wav
    sound = AudioSegment.from_mp3(os.getcwd() + "\\sample.mp3")
    sound.export(os.getcwd() + "\\sample.wav", format="wav")
    sample_audio = sr.AudioFile(os.getcwd() + "\\sample.wav")
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    MyText = r.recognize_google(audio)
    print(MyText)
    time.sleep(0.5)
    driver.find_element(By.ID, "audio-response").send_keys(MyText)
    time.sleep(0.5)
    driver.find_element(By.ID, "recaptcha-verify-button").click()
    driver.switch_to.default_content()
    time.sleep(1)
    driver.find_element(By.ID, "recaptcha-demo-submit").click()


main()
