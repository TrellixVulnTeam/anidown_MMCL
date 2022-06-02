from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getinfo
import json
import os
import argparse




def wait():
    """
    sleep for 2 seconds (made by tinolm)
    """
    sleep(2)


cache = {}
with open("cache.json", 'r') as f:
    cache = json.load(f)




link = getinfo.get_link()
if link == "":
    link = cache[len(cache)]
    print(link)

ep = input("Episode: ")
if str(ep) == " ":
    ep = getinfo.get_episode(link)

else:
    ep = int(ep)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
print("disabled notifications")
chrome_options.add_extension("./adbp.crx")
chrome_options.extensions()
print("loaded extension")
driver = webdriver.Chrome("./chromedriver")







def getit(target):

    driver.implicitly_wait(5)

    driver.get(target)
    #hosters = driver.find_element_by_class_name("watchEpisode")



    #print(hosters)
    #hosters.click()
    #driver.switch_to_window(driver.window_handles[0])
    #hosters.click()

    #get the right hoster
    streamtape = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/ul/li[2]/div/a/div')
    try:
        streamtape.click()#Click Hoster button streamtape
    except:
        ad = driver.find_element_by_xpath()
        pass

    sleep(3)#wait for everything to be loaded
    play = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/div[2]/div[1]/iframe')#find the player iframe using xpath
    #everything else was to hard to get
    
    
    
    #try to detect a captcha
    



    play.click()#get faked on purpose
    videpframe = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[2]/div[3]/div[5]/div[2]/div[1]/iframe').get_attribute('src')#
    print(play)
    print(videpframe)
    driver.switch_to_window(driver.window_handles[0])
    print("Wait for it too load")

    play.click()#play video

    play.click()#pause video
    driver.switch_to_window(driver.window_handles[0])

    play.click()

    #all set up OPEN THE PAGE
    driver.get(videpframe)
    sleep(3)
    print(driver.current_url)
    if "redirect" in driver.current_url:
        os.system('notify-send "Captcha PLS SOLVE!!!"')
        driver.maximize_window()
        print("Captcha shit")
        
        
        input("Press enter when done")#wait for user to finish the captcha


        driver.minimize_window()

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
while True:
    newep = getit(link.replace(f"-{ep}", f"-{ep+a}"))

    
    a += 1
    #save ep link
    epss[a] = newep
    with open ("eps.json", 'w') as f:
        json.dump(epss, f)
    


""" Example stuff, helpful
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""

