import webbrowser

class Browser:
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