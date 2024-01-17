from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login(browser):
    browser.get("https://www.instagram.com/?hl=en")
    
    browser.find_element(By.XPATH, '//button[contains(text(), "Allow all cookies")]').click()

    time.sleep(5)

    username = browser.find_element(By.CSS_SELECTOR, "[name='username']")
    password = browser.find_element(By.CSS_SELECTOR, "[name='password']")
    login = browser.find_element(By.CSS_SELECTOR, "button")

    #YOUR USERNAME GOES HERE
    username.send_keys("")
    #YOUR Password GOES HERE
    password.send_keys("")
    login.click()

    time.sleep(10)

    browser.find_element(By.XPATH, '//div[contains(text(), "Not now")]').click()

def Vist_Tag(browser, url):
    sleepy_time = 6
    browser.get(url)
    time.sleep(sleepy_time)

    pictures = browser.find_elements(By.CSS_SELECTOR, "div[class='_aagw']")

    image_count = 0

    for picture in pictures:
        if image_count >= 15:
            break

        picture.click()
        time.sleep(sleepy_time)

        browser.find_element(By.CSS_SELECTOR, "[aria-label='Like']").click()
        browser.find_element(By.CSS_SELECTOR, "svg[aria-label='Close']").click()

        image_count += 1
        time.sleep(sleepy_time)

def main():
    browser = webdriver.Chrome()
    login(browser)

    tags = [ 
    #   "yoga",
        # "yogapose",
        # "wheelpose",
        # "yogabackbend",
    #     "polishgirl",
    #     "aloyoga",
    #     "oysho",
    #     "stretch",
    #     "yogainspiration",
         "yogaaesthetic",
         "wellnessgoals",
         "healthandwellness",
         "yogaflow",
    #     "yogaprogress",
    #     "yogapractice",
    #     "yogainspo",
    #     "polskadziewczyna",
    #     "polskakobieta",
    #     "blondie",
    #     "blond",
    #     "blondme",
    #     "blondebalayage",
    #     "polishmodel",
    #     "bizuteriaapart",
    #     "outfits",
    #     "jewellery",
    #     "wspolpraca"
    ]

    while True:
        for tag in tags:
            Vist_Tag(browser, f"https://www.instagram.com/explore/tags/{tag}")
        time.sleep(3600)

main()