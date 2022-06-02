import os
import requests
import tarfile
import zipfile

def download(filename, url):#make a download fuction
    with open(filename, "wb") as f:
        target = requests.get(url)
        f.write(target.content)

#Dowload anidown
download("main-firefox.py", "https://raw.githubusercontent.com/learning-thing/anidown/master/main-firefox.py")#get the main file
download("getinfo.py", "https://raw.githubusercontent.com/learning-thing/anidown/master/getinfo.py")#get a library
download("diff_adder.py", "https://raw.githubusercontent.com/learning-thing/anidown/diff_adder.py")#get another library

#download browser stuff
sos = int(input("windows[1] / linux[2]?: "))
if sos == 1:
    download("geckodriver.zip", "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-win64.zip")
    print("please extract/unzip geckodriver.zip")
    with zipfile.ZipFile("geckodriver.zip") as f:
        f.printdir()#print(content)

        f.extractall()#extract file


if sos == 2:
    download("geckodriver.tar.gz", "https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz")
    #print("please extract/unzip geckodriver.tar.gz")
    #extract file
    with tarfile.open("geckodriver.tar.gz") as sas:
        sas.extractall()

download("adbp.xpi", "https://addons.mozilla.org/firefox/downloads/file/3956140/adblock_plus-3.14.xpi")#download ad block plus




sos = int(input("python3[1] / python[2]?: "))
if sos == 1:
    os.system("python3 -m pip install -U selenium")

if sos == 2:
    os.system("python -m pip install -U selenium")

#create some files
with open("cache.json", "w") as f:
    print("created cache file")
    f.write('{"1": "https://aniworld.to/anime/stream/death-note/staffel-1/episode-1"}')
with open("eps.json", "w") as f:
    f.write('{"1": "https://aniworld.to/anime/stream/death-note/staffel-1/episode-1"}')
    print("created eps file")






print("installer finished, exiting....")