from enum import Enum

class Type(Enum):
    ANIME = "anime",
    MANGA = "manga"

class Anime():
    __title = None 
    __type = None
    __url = None
    __pageIdentifier = None
    __episodeUrls = [] #[{url1:False, url2:False,...}]
    __totalEpisodes = None
    __watched = None

    def __init__(self, title:str, type:Type, url:str, pageIdentifier:str, episodeUrls:str, totalEpisodes:int, watched:bool):
        self.__title = title 
        self.__type = type
        self.__url = url
        self.__pageIdentifier = pageIdentifier
        self.__episodeUrls = episodeUrls
        self.__totalEpisodes = totalEpisodes
        self.__watched = watched
        #TODO: raise error (here) if any of the are none 

    def get_dataAsDict(self):
        return {
            "name" : self.__title,
            "type" : self.__type,
            "originalUrl" : self.__url,
            "pageIdentifier" : self.__pageIdentifier,
            "episodeUrls" : self.__episodeUrls,
            "totalEpisodes" : self.__totalEpisodes,
            "watched" : self.__watched
        }

anime = Anime(
    title = None ,
    type = None,
    url = None,
    pageIdentifier = None,
    episodeUrls = [], #[{url1:False, url2:False,...}]
    totalEpisodes = 10,
    watched = True
)

print(anime.get_dataAsDict())