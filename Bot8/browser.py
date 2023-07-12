from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


class Device:
    name = ""
    hight = 800
    width = 600

    def driver(self, hight, width):
        self.hight = hight
        self.width = width
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--window-size={},{}".format(self.hight, self.width))
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        )
        # just some options passing in to skip annoying popups
        options.add_argument(
            "--no-first-run --no-service-autorun --password-store=basic"
        )

        options.accept_insecure_certs = True
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        return driver
