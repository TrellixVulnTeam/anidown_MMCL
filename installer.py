from os import system
import requests

def download(filename, url):
    with open(filename, "wb") as f:
        target = requests.get(url)
        f.write(target.content)

download("main-firefox.py", "https://raw.githubusercontent.com/learning-thing/anidown/master/main-firefox.py")#get the main file
download("getinfo.py", "https://raw.githubusercontent.com/learning-thing/anidown/master")