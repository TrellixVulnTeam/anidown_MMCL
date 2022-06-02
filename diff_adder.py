from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getinfo
import json
import os



#get arguments
os.system("cd /home/pcadmin/Programme/anicloud")

def wait():
    """
    sleep for 2 seconds (made by tinolm)
    """
    sleep(2)

print(getinfo.get_last_link())

cache = {}
with open("cache.json", 'r') as f:
    cache = json.load(f)

link = getinfo.get_link()
if link == "":
    link = cache[len(cache)]
    print(link)

"""
ep = input("Episode: ")#get episode
if str(ep) == "":
    ep = getinfo.get_episode(link)

else:
    ep = int(ep)
"""

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser-stable"

print("loaded extension")
driver = webdriver.Chrome(executable_path="/home/pcadmin/Programme/anicloud/chromedriver", chrome_options=options)


cache = {}
with open("cache.json", 'r') as f:
    cache = json.load(f)



def getit(target):

    driver.implicitly_wait(5)

    driver.get(target)
    try:
        dood = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/ul/li[3]/div/a/div')
    except:
        print("oh shit an ad appeared")
        pass

    sleep(3)#wait for everything to be loaded

    try:
        videpframe = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/div[2]/div[1]/iframe').get_attribute('src')#
    except Exception as e:
        print(e)
        driver.quit()
    #print(play)


    print(videpframe)
    driver.switch_to_window(driver.window_handles[0])
    print("Wait for it too load")

    driver.switch_to_window(driver.window_handles[0])


    #all set up OPEN THE PAGE
    driver.get(videpframe)
    sleep(3)
    print(driver.current_url)
    
    if "redirect" in driver.current_url:
        os.system('notify-send "Captcha PLS SOLVE!!!"')
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
            os.system("zsh -c 'java -jar ~/Programme/fertige\ Programme/JDOWNLOADER\ VIDS/JDOWNLOADERYAAAY/JDownloader.jar $(cat eps.json)' &")
            exit()
            
        else:
            exit(0)
