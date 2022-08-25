from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service




ani_link = str(input("Link: "))

def Get_EP(link):
    if ("aniworld.to" in link):
        print("Link accepted")

    else:
        print("wrong link")
        exit(1)

    chrome_options = webdriver.FirefoxOptions()
    extension_path = './adbp.xpi'
    s = Service("./geckodriver")
    driver = webdriver.Firefox(service=s)
    driver.install_addon(extension_path, temporary=False)
    driver.get(link)
    sleep(5)
    driver.switch_to.window('main')
    


    #Load page

        
Get_EP(ani_link)
