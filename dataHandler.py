import os, json
from serverCommunication import get_client
from config import data_path
from config import ipaddress, username, privKeyfile_windows, DATAPATH_SERVER, base_dir
from config import windows, termux, linux
from serverCommunication import windowsClient, termuxClient

from utils import get_operatingSystem

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

def DataHander():
    data = None
    datafile_path = None

    def __inti__(self, datafile_path):
        #load data 
        self.datafile_path = datafile_path
        load_data()

    def fetch_dataFromServer(self):
        # get data from server
        opSys = get_operatingSystem()
        client = get_client(opSys)
        client.get_file(ipaddress, username, DATAPATH_SERVER, os.path.dirname(self.datafile_path))

    def load_data(self):

        fetch_dataFromServer()

        # open data file
        try:
            with open(self.datafile_path) as file:
                data = json.load(file)
        except:
            data = {}
        self.data = data
        return True 

    def save_data(self, data:dict):
        # save changes to file
        with open(self.datafile_path, "w") as file:
            json.dump(data, file, indent=4)
        # transder file to server
        opSys = get_operatingSystem()
        client = get_client(operatingSystem=opSys)
        client.transfer_file(ipaddress, username, self.datafile_path, os.path.dirname(DATAPATH_SERVER))

    def get_data(self):
        return self.data

def gen_episodeUrls(episodeUrl, pageIdentifier, MAX_EPISODES, watchedEpisodes):
    #identifying page within pageIdentifier
    #AXIOM 1: only collective numbers are possinle within the complete pageIdentifier
    episodeNr = ""
    for char in pageIdentifier:
        if char.isdigit():
            episodeNr += char
    urls = {}
    for i in range(1, MAX_EPISODES+1): #correc +1, cause range, goes only to max-1
        new_pageIdent = pageIdentifier.replace(episodeNr, str(i)) 
        new_url = episodeUrl.replace(pageIdentifier, new_pageIdent)
        if i <= watchedEpisodes:
            urls[new_url] = 1
        else:
            urls[new_url] = 0
    return urls





