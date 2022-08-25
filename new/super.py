from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


ani_link = str(input("Link: "))
epi = int(input("Episode: "))
chrome_options = webdriver.FirefoxOptions()
extension_path = './adbp.xpi'
s = Service("./geckodriver")
driver = webdriver.Firefox(service=s)
driver.install_addon(extension_path, temporary=False)


veryfied = 0

def clear_file():
    with open("eps-txt", w) as f:
        empty = {}
        f.write(empty)

def save(line):
    with open("eps.txt", "a+") as f:
        data = f.read(100)
        print(str(data))
        f.write(line)
        f.write("\n")
        f.write("\n")

        


def gotit(line):
    try:
        with open("eps.txt", "r") as f:
            print(f)
            if line in f:
                print("Got this link already")
                return True
            else:
                return False
    except:
        with open("eps.txt", "a+") as f:
            f.write("\a")


driver.get(ani_link)


def Get_EP(link):
    last = link
    if "aniworld.to" in driver.current_url:
        sleep(4)
        last = driver.current_url
        if ("aniworld.to" in driver.current_url) and ("episode-" in driver.current_url) and (last == driver.current_url):
            print(driver.current_url)
            last = driver.current_url
            vidFRAME = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[3]/div/a').get_attribute("href")
            driver.get(vidFRAME)

    if "tape" in driver.current_url:
        if gotit(driver.current_url) == False:
            save(driver.current_url)#one saved
            veryfied += 1
        else:
            driver.get(link)
            sleep(2)
            
#Load page
newep = epi-1
veryfied = newep

while True:
    try:
        if newep == veryfied:
            newep += 1
            print("Veryfied, getting new")
        ani_link = ani_link.replace(f"ode-{str(newep-1)}", f"ode-{str(newep)}")
        print("Generated next link: ", ani_link)
        Get_EP(ani_link)
        print("Getting episode: ",newep)
    except KeyboardInterrupt:
        print("Ok, I am stopping for now :)")
