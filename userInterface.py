
def add_newAnime(watchUrl:str, title:str, pageIdentifier:str, episodesInTotal:int):

    return {
        title : {
            "type" : None,
            "originalUrl" : watchUrl,
            "pageIdentifier" : pageIdentifier,
            "episodeUrls" : [], #[{url1:False, url2:False,...}]
            "totalEpisodes" : episodesInTotal,
            "watched" : None
        }
    }

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