from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getinfo
import json
import os
import selenium



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
fp = webdriver.FirefoxProfile()
extension_path = '/home/pcadmin/Programme/anicloud/adbp.xpi'
print("loaded extension")
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.install_addon(extension_path, temporary=True)

cache = {}
with open("cache.json", 'r') as f:
    cache = json.load(f)

def getit(target):
    driver.implicitly_wait(5)
    driver.get(target)
    #hosters = driver.find_element_by_class_name("watchEpisode")

    #print(hosters)
    #hosters.click()
    #driver.switch_to_window(driver.window_handles[0])
    #hosters.click()

    #get the right hoster
    try:
        dood = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/ul/li[3]/div/a/div')
        #streamtape = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/ul/li[2]/div/a/div')#old
        #streamtape = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[1]/div/a/div')#new
        dood.click()#Click Hoster button streamtape
    except:
        print("oh shit an ad appeared")
        pass

    sleep(3)#wait for everything to be loaded
    
    """ only for streamtape
    #play = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/div[2]/div[1]/iframe')#find the player iframe using xpath
    try:
        play = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[6]/div/a/div')
    except selenium.common.exceptions.UnexpectedAlertPresentException as e:
        play = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[5]/ul/li[6]/div/a/div')
        print(e)
    #everything else was to hard to get
    
    #try to detect a captcha
    
    print("\n")
    print("clicking player")
    print("\n")
    try:
        play.click()#get faked on purpose
        
    except:
        try:
            play.click()
        except:
            pass
    """
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
    os.system(f"notify-send {driver.current_url}")
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

