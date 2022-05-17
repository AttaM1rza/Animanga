import os
from config import windows, linux
from config import privKeyfile_windows
from utils import get_operatingSystem

def get_client(operatingSystem):
    if operatingSystem==windows:
        return windowsClient()
    elif operatingSystem == linux:
        return termuxClient()

class termuxClient():
    
    def login_toServer(self, ipaddress:str, username:str):
        command = f"ssh {username}@{ipaddress}"
        os.system(command)

    def get_file(self, ipaddress:str, username:str, fromServerFilepath:str, toLocalFolderpath:str):
        command = f"scp {username}@{ipaddress}:{fromServerFilepath} {toLocalFolderpath} "
        os.system(command)

    def transfer_file(self, ipaddress:str, username:str, fromLocalFilepath:str, toServerFolderpath:str):
        command = f"scp {fromLocalFilepath} {username}@{ipaddress}:{toServerFolderpath}"
        os.system(command)

class windowsClient():

    def login_toServer(self, ipaddress:str, username:str):
        privKey_path = os.path.join(r"C:\Users\Atta\.ssh", privKeyfile_windows)
        command = f"ssh -i {privKey_path} {username}@{ipaddress}"
        os.system(command)

    def get_file(self, ipaddress, username, fromServerFilepath, toLocalFolderpath):
        privKey_path = os.path.join(r"C:\Users\Atta\.ssh", privKeyfile_windows)
        command = f"scp -i {privKey_path} {username}@{ipaddress}:{fromServerFilepath} {toLocalFolderpath} "
        os.system(command)

    def transfer_file(self, ipaddress:str, username:str, fromLocalFilepath:str, toServerFolderpath:str):
        privKey_path = os.path.join(r"C:\Users\Atta\.ssh", privKeyfile_windows)
        command = f"scp -i {privKey_path} {fromLocalFilepath} {username}@{ipaddress}:{toServerFolderpath}"
        os.system(command)

#TODO: class termuxClient():