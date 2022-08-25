from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


ani_link = str(input("Link: "))
epi_start = int(input("Episode start: "))
epi_end = int(input("Episode end: "))
chrome_options = webdriver.FirefoxOptions()
extension_path = './adbp.xpi'
s = Service("./geckodriver")
driver = webdriver.Firefox(service=s)
driver.install_addon(extension_path, temporary=False)


def clear_file():
    with open("eps.txt", "w") as f:
        empty = ""
        f.write(empty)

clear_file()


def save(line):
    with open("eps.txt", "a+") as f:
        data = f.read(100)
        print(str(data))
        f.write("\n")
        f.write(line)

def Get_EP(link):
    driver.get(link)
    print(driver.current_url)
    vidFRAME = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[3]/div/a').get_attribute("href")
    driver.get(vidFRAME)
    while "tape" not in driver.current_url:
        print("waiting for streamtape")
        sleep(1)
    print(driver.current_url)
    save(driver.current_url)


link_list = []
#generate all episode links
for i in range(epi_start, epi_end+1):
    link_list.append(ani_link+f"/episode-{i}")
    print(link_list)
    print("\n")

driver.switch_to.window(driver.window_handles[0])
for i in link_list:
    Get_EP(i)


driver.quit()
ani_link = ani_link.replace("https://aniworld.to/anime/stream/", "")
ani_link = ani_link.replace("-", " ")





print(f"Downloaded: {ani_link}")
print("from " + str(epi_start))
print("to " + str(epi_end))