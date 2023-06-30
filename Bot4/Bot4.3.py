import time
from bs4 import BeautifulSoup
import os
from twocaptcha import TwoCaptcha
from dotenv import load_dotenv
import requests

load_dotenv()
sitekey = "6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-"
url = "https://www.google.com/recaptcha/api2/demo"
solver = TwoCaptcha(os.getenv("API"))


def get_cookie(url):
    response = requests.get(url)
    cookies = response.cookies
    return cookies


def solve(url, sitekey):
    result = solver.recaptcha(sitekey, url)
    return result.get("code")


def post_page(url, result, cookies):
    paylaod = "g-recaptcha-response = {}"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.google.com/recaptcha/api2/demo",
    }
    response = requests.post(
        url, paylaod.format(result), headers=headers, cookies=cookies
    )
    soap = BeautifulSoup(response.text, "lxml")
    # el = soap.select_one("body > div")
    return soap


def main():
    # time.sleep(120)
    cookies = get_cookie(url)
    print("cookies: ", cookies)
    result = solve(url, sitekey)
    print("captcha solve: ", result)

    # time.sleep(12)
    data = post_page(url, result, cookies)
    print(data)


main()
