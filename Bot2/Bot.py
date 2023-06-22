from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# need to install webdriver manager


def main():
    proxy = "14.231.161.89:8080"  # desired proxy ip with port
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--proxy-server=%s" % proxy)
    # options.accept_insecure_certs = True
    # options.add_argument()
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get("https://www.showmyip.com/")

    # driver.close()


main()
