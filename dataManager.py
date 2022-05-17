import os, json
from serverCommunication import get_client
from config import data_path
from config import ipaddress, username, privKeyfile_windows, DATAPATH_SERVER, base_dir
from config import windows, termux
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

def gen_episodeUrls(episodeUrl, pageIdentifier, MAX_EPISODES):
    #identifying page within pageIdentifier
    #AXIOM 1: only collective numbers are possinle within the complete pageIdentifier
    episodeNr = ""
    for char in pageIdentifier:
        if char.isdigit():
            episodeNr += char
    urls = {}
    for i in range(1, MAX_EPISODES+1):
        new_pageIdent = pageIdentifier.replace(episodeNr, str(i)) 
        new_url = episodeUrl.replace(pageIdentifier, new_pageIdent)
        urls[new_url] = 0
    return urls

def save_data(file_path, data:dict):
    # save changes to file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    # trnasfer file to server
    opSys = get_operatingSystem()
    client = get_client(operatingSystem=opSys)
    client.transfer_file(ipaddress, username, data_path, os.path.dirname(DATAPATH_SERVER))

def load_data(file_path):
    # get data from server
    opSys = get_operatingSystem()
    client = get_client(opSys)
    client.get_file(ipaddress, username, DATAPATH_SERVER, os.path.dirname(data_path))

    # open data file
    try:
        with open(file_path) as file:
            data = json.load(file)
    except:
        data = {}
    
    return data

