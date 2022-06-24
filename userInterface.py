from anime import Anime
def add_newAnime(watchUrl:str, title:str, pageIdentifier:str, episodesInTotal:int):

    #{
    #     title : {
    #         "type" : None,
    #         "originalUrl" : watchUrl,
    #         "pageIdentifier" : pageIdentifier,
    #         "episodeUrls" : [], #[{url1:False, url2:False,...}]
    #         "totalEpisodes" : episodesInTotal,
    #         "watched" : None
    #     }
    # }
    return None 

def get_userInp_addAnime():
    url = input("ENTER THE URL, TO WATCH THE ANIME: ")
    title = input("ENTER THE TITLE OF THE ANIME: ")
    pageIdentifier = input("ENTER THE PAGE-IDENTIFIER WHICH IS WITHIN THE URL \n (meaning the substring in the url wich is used to navigate through the espisodes): ")
    episodesInTotal = int(input("ENTER THE AMOUNT OF THE EPISODES: "))
    episodesWatched = int(input("enter how many episodes are already WATCHED (0,1,2...): "))
    
    newAnime = Anime(title=title, type=None, url = watchUrl,
    pageIdentifier=pageIdentifier, episodeUrls=[], #[{url1:False, url2:False,...}]
    totalEpisodes=episodesInTotal, totalWatchedEpisodes=episodesWatched,
    watched=False
    )
    return newAnime

def display_disclaimer():
    print(
    """
    ---------------------------------------------

    welcome to animanga's user interface!
    watch convinient and fast your favourite animes
    by just few clicks. start from where you left,
    without to search or remember where you stopped 
    watching.

    ---------------------------------------------
    """
    )

# def display_menu():
#     print("""    
#     WHAT DO YOU WANT TO DO ?
#     + [1] watch anime!
#     + [2] add a new anime

#     + [0] exit
#     """)    

def show_allAnimes(animes:dict):
    for i, name in enumerate(animes.keys()):
        print(f"[{i}] - {name}")

def watchMODE():
    print("\n")
    print("   DID YOU FINISHED WATCHING THIS EPISODE ?")
    print("   [1] YES & CONTINUE   [2] yes & GO BACK   [0] no & GO BACK")
    answer = int(input(">> "))  
    if answer == 1:return 1
    if answer == 2:return 2
    if answer == 0:return 0

    #TODO: if watchlist completed set watched to True