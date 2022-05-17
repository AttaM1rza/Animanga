import os

base_dir = os.path.dirname(__file__)

#CONST
#all host systems where this code can run
windows = "WINDOWS"
linux = "LINUX"
termux = "TERMUX"
DATAPATH_SERVER = "/home/atta/animanga/data.json"


# VARIABLES
ipaddress = "140.82.36.17"
username = "root"
privKeyfile_windows = "id_rsa_vultrPriv"

#FOLDERS
data_folder = os.path.join(base_dir, "data.json")

#FILES
data_path = os.path.join(base_dir, "data.json")


