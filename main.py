from mmap import PAGESIZE
import webbrowser, os, json, queue
from utils import get_operatingSystem, internet_is_active
from config import data_path, WAIT_INTERNETERROR
from config import windows, linux, termux
import time 

from userInterface import add_newAnime, show_allAnimes, watchMODE, display_disclaimer
from dataHandler import load_data, save_data, gen_episodeUrls
from browser import get_browserClient

"""
README: 
-episodes are synonyms of chapters of an mangas or episodes of animes
-here is the anime used for anime and mangas ____
-watchlist contains all animes and mangas as an dict. the keys represent the name of an anime or manga

TODO:
-generate complete url links and save them 
-to make sure that new released episodes are also updated, scrape the site to get the max amount of episodes
and after that insert the max total episode amount into data (totalEpisodes) and run before watching any episode 
the method, which generates episode urls.
-
"""

def add_newAnime_logic(data):
    #add new Entry
            url = input("ENTER THE URL, TO WATCH THE ANIME: ")
            title = input("ENTER THE TITLE OF THE ANIME: ")
            pageIdentifier = input("ENTER THE PAGE-IDENTIFIER WHICH IS WITHIN THE URL \n (meaning the substring in the url wich is used to navigate through the espisodes): ")
            episodesInTotal = int(input("ENTER THE AMOUNT OF THE EPISODES: "))
            episodesWatched = int(input("enter how many episodes are already WATCHED: "))
            newEntry = add_newAnime(url, title, pageIdentifier, int(episodesInTotal))
            #TODO: get urls for every episode and add to dict

            newEntry_key = list(newEntry.keys())[0]
            newEntry_value = newEntry[newEntry_key]
            data[newEntry_key] = newEntry_value

            data[newEntry_key]["episodeUrls"] = gen_episodeUrls(
                data[newEntry_key]["originalUrl"], 
                data[newEntry_key]["pageIdentifier"],
                data[newEntry_key]["totalEpisodes"],
                episodesWatched
            )

            #save it
            while not internet_is_active():
                continue
            save_data(file_path=data_path, data=data)

def select_episode(anime):
    #CASE: new episodes where published (scraper needs to be implemented) #TODO: get urls for every episode and add to dict
    

    #CASE: urls are empty
    notWatchedEp = None
    allEpisodes = anime["episodeUrls"] #getting dicts as list [{url:bool}, {url2:bool2}]
    for episode in allEpisodes.keys():
        if allEpisodes[episode] == False: #TODO: BUG
            notWatchedEp = episode
            break
    
    return notWatchedEp 


def main():

    display_disclaimer()
    while not internet_is_active():
        continue
    #load complete data
    data = load_data(data_path)
    operatingSys = get_operatingSystem()
    Br = get_browserClient(operatingSys)

    keepMenu = True
    while(keepMenu):
        print("")
        print("[-1] - to EXIT this program\n")
        #show all availible animes & choose from it
        show_allAnimes(data)
        print("")
        print("ENTER [0] to add a new Anime")
        print("or")
        print("ENTER [n] index number from above to watch")
        user_input=None
        while((user_input==None) or (user_input=='')):
            user_input = input("\n>>> ")
        user_choice = int(user_input)
        if user_choice == -1: break
        elif user_choice == 0:
            add_newAnime_logic(data)
        elif not (1 <= user_choice and user_choice < len(list(data))):
            print("Input was invalid!")
            continue
        else:
            animename = list(data)[user_choice]

            keepWatching = True
            while(keepWatching):
                episodeUrl = select_episode(data[animename])
                if not episodeUrl:
                    print("\n\n[+] EPISODE WATCHLIST IS EMPTY! (already watched everything)")
                    #print("\n" *1)
                    time.sleep(5)
                    break #go back to menue
                
                Br.open_window(episodeUrl)
                watchResult = watchMODE()
                if watchResult==1 or watchResult==2:
                    data[animename]["episodeUrls"][episodeUrl] = 1 #mark it as WATCHED
                    while not internet_is_active():
                        continue
                    save_data(data_path, data)
                    if watchResult==2:
                        keepWatching = False
                else: #go back to menu
                    keepWatching = False 

    return None 

if __name__ == "__main__" : 
    main()