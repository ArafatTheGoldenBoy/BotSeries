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
        options.accept_insecure_certs = True
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        return driver


def main():
    user1 = Device()
    user2 = Device()

    driver = user1.driver(900, 700)
    driver.get("https://google.com")

    time.sleep(1)

    driver2 = user2.driver(700, 900)
    driver2.get("https://youtube.com")
    # driver.close()


main()
