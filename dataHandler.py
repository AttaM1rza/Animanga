import os, json
from serverCommunication import get_client
from config import data_path
from config import ipaddress, username, privKeyfile_windows, DATAPATH_SERVER, base_dir
from config import windows, termux, linux
from serverCommunication import windowsClient, termuxClient
from utils import internet_is_active

from utils import get_operatingSystem
from anime import Anime

"""

newData = {
    name : {
            "type" : None,
            "originalUrl" : url,
            "pageIdentifier" : pageIdentifier,
            "episodeUrls" : [], #[{url1:False, url2:False,...}]
            "totalEpisodes" : episodesInTotal,
            "watched" : None
        }
    }

"""

class DataHandler:
    data = None
    datafile_path = None

    def __init__(self, datafile_path):
        #load data 
        self.datafile_path = datafile_path
        #load_data()

    def __fetch_dataFromServer(self):
        # get data from server
        opSys = get_operatingSystem()
        client = get_client(opSys)
        client.get_file(ipaddress, username, DATAPATH_SERVER, os.path.dirname(self.datafile_path))

    def load_data(self):
        while not internet_is_active():
                continue

        self.__fetch_dataFromServer()

        # open data file
        try:
            with open(self.datafile_path) as file:
                data = json.load(file)
        except:
            data = {}
        self.data = data
        return True 

    def save_data(self, data:dict):
        while not internet_is_active():
                continue
        # save changes to file
        with open(self.datafile_path, "w") as file:
            json.dump(data, file, indent=4)
        # transder file to server
        opSys = get_operatingSystem()
        client = get_client(operatingSystem=opSys)
        client.transfer_file(ipaddress, username, self.datafile_path, os.path.dirname(DATAPATH_SERVER))

    def get_data(self):
        return self.data

    def add_anime(self, anime:Anime):
        self.data[anime.__title] = anime.get_dataAsDict
        return None 

    def delete_anime(self):

        return None 

    def get_anime(self, animeTitle):
        return self.data[animeTitle]

    def gen_episodeUrls(self, animeName, totalWatchedEpisodes):
        #identifying page within pageIdentifier
        #AXIOM 1: only collective numbers are possinle within the complete pageIdentifier
        animeData = self.get_anime(animeName)
        pageIdentifier = animeData["pageIdentifier"]
        MAX_EPISODES = animeData["totalEpisodes"]
        episodeUrl = animeData["originalUrl"]

        #get episodeNr within pageIdent
        episodeNr = ""
        for char in pageIdentifier:
            if char.isdigit():
                episodeNr += char
        
        #create urls based on pageIndent
        urls = {}
        for i in range(1, MAX_EPISODES+1): #correc +1, cause range, goes only to max-1
            new_pageIdent = pageIdentifier.replace(episodeNr, str(i)) 
            new_url = episodeUrl.replace(pageIdentifier, new_pageIdent)
            if i <= totalWatchedEpisodes:
                urls[new_url] = 1
            else:
                urls[new_url] = 0
        return urls







