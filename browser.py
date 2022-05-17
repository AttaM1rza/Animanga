from curses import window
import webbrowser, os
from config import windows, linux, termux

def get_browserClient(operatingSys):
    if operatingSys == windows:
        return Browser_windows
    elif operatingSys == termux:
        return termux
    elif operatingSys == linux:
        raise ValueError("NOT IMPLEMENTED YET")
    raise ValueError("COULD NOT FIND BROWSER !")

class Browser_windows:
    # SET UP WEBBROWSER SETTINGS:
    operaExe = r"C:\Users\Atta\AppData\Local\Programs\Opera\launcher.exe"
    browsername = "opera"

    def __init__(self):
        browserClassInstance = webbrowser.Opera(self.operaExe)
        webbrowser.register(self.browsername, None, browserClassInstance)

    def open_window(self, url):
        webbrowser.get(self.browsername).open_new(url)

    def open_Tab(self, url):
        webbrowser.get(self.browsername).open_new_tab(url)

class Browser_termux:

    def open_window(self, url):
        os.system(f"termux-open-url {url}")

    def open_Tab(self, url):
        self.open_window(url)