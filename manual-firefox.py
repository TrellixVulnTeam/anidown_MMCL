from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.by import By
from time import sleep
import getinfo
import json
import os
import selenium
from selenium.webdriver.chrome.service import Service


#get arguments

os.system("cd /home/pcadmin/Programme/anicloud")

def wait():
    """
    sleep for 2 seconds (made by tinolm)
    """
    sleep(2)

try:
    print(getinfo.get_last_link())
except:
    print(" ")

cache = {}
try:
    with open("cache.json", 'r') as f:
        cache = json.load(f)
except:
    with open("cache.json", "r") as f:
        print("created cache file")


link = getinfo.get_link()
if link == "l":
    try:
        link = cache[len(cache)]
        print("last link: " + link)
    except:
        print("failed to print last used link")


ep = input("Episode: ")#get episode
if str(ep) == "":
    ep = getinfo.get_episode(link)

else:
    ep = int(ep)


chrome_options = webdriver.FirefoxOptions()
extension_path = './adbp.xpi'

s = Service("./geckodriver")
driver = webdriver.Firefox(service=s)
driver.install_addon(extension_path, temporary=True)

cache = {}
with open("cache.json", 'r') as f:
    cache = json.load(f)

def getit(target):
    driver.implicitly_wait(5)
    driver.get(target)


    #get the right hoster
    print("Click Streamtape")
    sleep(5)#wait for everything to be loaded
    
    try:
        #xpath 
        videpframe = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[3]/div/a')
        
        print(videpframe)

        videpframe = videpframe.get_attribute("href")
        print(videpframe)
        driver.get(videpframe)
        sleep(10)

    #print(play)
    except Exception as e:
        print(e)

    print(videpframe)
    driver.switch_to_window(driver.window_handles[0])
    print("Wait for it too load")

    driver.switch_to_window(driver.window_handles[0])


    #all set up OPEN THE PAGE
    driver.get(videpframe)
    sleep(3)
    print(driver.current_url)
    os.system(f"notify-send {driver.current_url}")
    sleep(5)
    if "redirect" in driver.current_url:
        #driver.maximize_window()
        print("Captcha shit")
        cap_handled = False
        
        #input("Press enter when done")#wait for user to finish the captcha

        capchad = False
        while capchad == False:
            sleep(0.1)
            if "redirect" in driver.current_url:
                capchad = False
            else:
                capchad = True
                break

        #driver.minimize_window()

    print(driver.current_url)
    with open("eps.json", "r") as f:
        print(f.read)

    return driver.current_url
    driver.delete_all_cookies()
    driver.close()
    driver.quit()





#Loop to download all episodes (seasons not included yet
# )
a = 0
epss = {

}
done = False
while True:
    try:
        print(link.replace(f"e-{ep}", f"e-{ep+a}"))
        newep = getit(link.replace(f"e-{ep}", f"e-{ep+a}"))

        
        a += 1
        #save ep link
        epss[a+ep] = newep
        with open ("eps.json", 'w') as f:
            json.dump(epss, f)
        
        
        cache[len(cache)+1] = str(link.replace(f"e-{ep}", f"e-{ep+a}"))


        with open("cache.json", 'w') as f:
            json.dump(cache, f)
    except:
        if done == False:
            done == True
            #os.system("zsh -c 'java -jar ~/Programme/fertige\ Programme/JDOWNLOADER\ VIDS/JDOWNLOADERYAAAY/JDownloader.jar $(cat eps.json)' &")
            exit()
            
        else:
            exit(0)


""" Example stuff, helpful
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""

