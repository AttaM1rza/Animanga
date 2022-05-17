from config import windows, linux, termux
import platform, os

def get_operatingSystem():
    if platform.system() == "Windows":
        return windows
    elif platform.system() == "Linux" and os.getcwd().find("termux")!=-1:
        return termux
    elif platform.system() == "Linux":
        return linux 
    else:
        raise ValueError("COULD NOT RECOGNIZE OS")
    return None