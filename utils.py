from config import windows, linux, termux
import platform

def get_operatingSystem():
    if platform.system() == "Windows":
        return windows
    if platform.system() == "Linux":
        return termux
    return None