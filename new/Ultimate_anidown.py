from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


ani_link = str(input("Link: "))

if "staffel" in ani_link:
    if ani_link[-1] == "/":
        ani_link = ani_link+f"staffel-{staffel}/"
    else:
        ani_link = ani_link+f"/staffel-{staffel}/"

else:
    staffel = str(input("Staffel?"))
    if ani_link[-1] == "/":
        ani_link = ani_link+f"staffel-{staffel}/"
    else:
        ani_link = ani_link+f"/staffel-{staffel}/"


if "episode" in ani_link:
    try:
        epi_start = int(input("Episode start: "))
    except ValueError:
        epi_start = int(1)

else:
    print("Episode not found in link")
    try:
        epi_start = int(input("Episode start: "))
    except ValueError:
        print("\n\n\n No episode given automatically guessing 1")

        epi_start = int(1)

    if ani_link[-1] == "/":
        ani_link = str(ani_link+f"episode-{epi_start}")
        print(ani_link)
    elif ani_link[-1] != "/":
        ani_link = ani_link+f"/episode-{epi_start}"
    print(ani_link)

try:
    epi_end = int(input("Episode end: "))
except ValueError:
    epi_end = epi_start



chrome_options = webdriver.FirefoxOptions()
extension_path = './adbp.xpi'
s = Service("./geckodriver")
driver = webdriver.Firefox(service=s)
driver.install_addon(extension_path, temporary=False)

#clear all temp links
def clear_file():
    with open("eps.txt", "w") as f:
        empty = ""
        f.write(empty)


#function to remember known anime links
def add_known_link():
    try:
        with open("AnimeList.txt", "r") as f:
            if ani_link not in f.read():
                with open("AnimeList.txt", "a+") as l:
                    l.write("\n")
                    l.write(ani_link)
                    l.write("\n")
    except:
        with open("AnimeList.txt", "w") as f:
            f.write("\n")
            f.write("\b")


#function to save episode links temporarely
def save(line):
    with open("eps.txt", "a+") as f:
        data = f.read(100)
        print(str(data))
        f.write("\n")
        f.write(line)


first = True
#Function to find anime episodes
def Get_EP(link, check_lang):
    driver.get(link)

    if check_lang == True:
        input("Check Lanbguage...")
        check_lang = False

    streamtape = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[3]/div/a')

    print(driver.current_url)


    vidFRAME = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[3]/div/a').get_attribute("href")
    #this is the streamtape button


    #Iframe
    #vidFRAME = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[5]/div[2]/div[1]/iframe').get_attribute("src")

    print(vidFRAME)
    driver.get(vidFRAME)
    while "tape" not in driver.current_url:
        print("waiting for streamtape")
        sleep(1)
    print(driver.current_url)
    save(driver.current_url)



#setup stuff
clear_file()
add_known_link()


link_list = []
#generate all episode links
for i in range(epi_start, epi_end+1):
    if ani_link[-1] != "/":
        link_list.append(ani_link+f"/episode-{i}")
    else:
        link_list.append(ani_link+f"episode-{i}")
    print(link_list)
    print("\n")

driver.switch_to.window(driver.window_handles[0])

first = True
for i in link_list:
    Get_EP(i, first)
    first=False


driver.quit()
ani_link = ani_link.replace("https://aniworld.to/anime/stream/", "")
ani_link = ani_link.replace("-", " ")
ani_link = ani_link.replace("/", " -- ")





print(f"Downloaded: {ani_link}")
print("from " + str(epi_start))
print("to " + str(epi_end))