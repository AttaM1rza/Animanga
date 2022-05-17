import json, os

base_dir = os.path.dirname(__file__)

#CONST
#all host systems where this code can run
windows = "WINDOWS"
linux = "LINUX"
termux = "TERMUX"
DATAPATH_SERVER = "/home/atta/animanga/data.json"


# VARIABLES
with open(os.path.join(base_dir, "serverAccess.json")) as file:
    serverCreds = json.load(file)
ipaddress = serverCreds["ipAddress"]
username = serverCreds["username"]
privKeyfile_windows = "id_rsa_vultrPriv"

#FOLDERS
data_folder = os.path.join(base_dir, "data.json")

#FILES
data_path = os.path.join(base_dir, "data.json")


