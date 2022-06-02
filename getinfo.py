import json

def get_link():
    print("Setting up information for download")

    link = str(input("Link to anicloud site: "))
    if "aniworld.to" not in link:
        print("incompatible link")
        exit()

    print(link)
    print(link[-1])

    if "episode-" not in link:
        print("incomplete link")
        print(link[-1])
        if link[-1] != "/":#check if link ends with slash
            link = f"{link}/staffel-1/episode-1"#add slash if not
            print(link)
        else:
            link = f"{link}staffel-1/episode-1"
    
    print(link)
    return link

def get_episode(urlel):
    if urlel[-1].isdigit():
        if urlel[-2].isdigit():
            epi = int(f"{urlel[-2]}{urlel[-1]}")
            print("episode: ",str(epi))
        else:
            epi = int(f"{urlel[-1]}")
            print("episode: ",str(epi))
    return epi


def get_ani_name():
    aniname = str(input("Name of the Anime"))

def get_last_link():
    try:
        link_json = {}
        with open("cache.json", 'r') as f:
            link_json = json.load(f)
        length = list(link_json)[-1]
        return link_json[length]
    except:
        return "0"
