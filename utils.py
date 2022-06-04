from config import windows, linux, termux
import platform, os, requests, time

def internet_is_active(waittime:int, raiseError:bool=False):
    url = "http://www.google.com"
    timeout = 5
    header = {"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    try:
        request = requests.get(url, timeout=timeout, headers=header)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        errorMessage = "[+] No internet connection established.\nPlease try again\n"
        print(errorMessage)
        time.sleep(waittime)
        if raiseError:
            raise ValueError(errorMessage)

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