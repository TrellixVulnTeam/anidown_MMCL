import os
import requests

def download(filename, url):
    with open(filename, "wb") as f:
        target = requests.get(url)
        f.write(target.content)

download("main-firefox.py", "https://raw.githubusercontent.com/learning-thing/anidown/master/main-firefox.py")#get the main file
download("getinfo.py", "https://raw.githubusercontent.com/learning-thing/anidown/master/getinfo.py")#get a library
download("diff_adder.py", "https://raw.githubusercontent.com/learning-thing/anidown/diff_adder.py")


sos = int(input("python3[1] / python[2]?: "))
if sos == 1:
    os.system("python3 -m pip install -U selenium")

if sos == 2:
    os.system("python -m pip install -U selenium")

