from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Add path to your own chromedriver on your pc(search it on google if you don't know it)
PATH = "C:\Program Files (x86)\chromedriver.exe"

link = input("Please add the link of your playlist")

driver = webdriver.Chrome(PATH)

driver.get(link)


def collectLinks():
    global songs_url
    songs_url = []
    playlist_titles = driver.find_elements_by_xpath("//ytd-thumbnail[@id='thumbnail']/a[@id='thumbnail']")
    for playlist_title in playlist_titles:
        songs_url.append(playlist_title.get_attribute("href"))


collectLinks()

driver.quit()

driver = webdriver.Chrome(PATH)
driver.get("https://ytmp3.cc/en13/")

for links in songs_url:

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "input"))
        )
    except:
        driver.close()

    search_box = driver.find_element_by_id("input")

    url_to_convert = links

    search_box.send_keys(url_to_convert)
    search_box.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Download"))
        )
    except:
        driver.close()

    convert_btn = driver.find_element_by_link_text("Download")
    convert_btn.click()

    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
