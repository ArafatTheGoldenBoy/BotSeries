import browser
import time
import os
import simpleaudio as sa
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    user1 = browser.Device()
    driver = user1.driver(1800, 900)
    driver.get("https://finance.yahoo.com/")
    target_price = 2600
    wave_obj = sa.WaveObject.from_wave_file(os.getcwd() + "\\alarm.wav")
    driver.find_element(By.NAME, ("reject")).click()
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    driver.find_element(By.ID, ("yfin-usr-qry")).send_keys("Natural Gas")
    time.sleep(1)
    driver.find_element(By.ID, ("header-desktop-search-button")).click()
    time.sleep(0.5)
    while True:
        time.sleep(20)
        driver.refresh()
        time.sleep(2)
        g = driver.find_element(
            By.XPATH,
            "//*[@id='quote-summary']/div[1]/table/tbody/tr[4]/td[2]",
        )
        print("target price: ", target_price)

        gas_price = int(float(g.text) * 1000)
        print("Gas price: ", gas_price)

        if gas_price >= target_price:
            print("peeep peep")
            play_obj = wave_obj.play()
            play_obj.wait_done()


main()
