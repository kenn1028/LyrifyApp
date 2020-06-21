from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from spotify_client import SpotifyAPI
# from lyrify_app import Ui_MainWindow
import time

class Worker(QObject):
    finished = pyqtSignal()
    song_update = pyqtSignal(str)

    @pyqtSlot()
    def update(self):
        while True:
            data = spotify.get_current_song_progress()
            # print(data)
            song_name = data["title"]

            # if ui.song_name_ != song_name:
            self.song_update.emit(song_name)
            self.finished.emit()

    def procCounter(self): # A slot takes no params
        for i in range(1, 100):
            time.sleep(1)
            self.intReady.emit(i)

        self.finished.emit()

# if __name__ == "__main__":
spotify = SpotifyAPI()
# ui = Ui_MainWindow()

try:
    spotify.perform_refresh()
except:
    spotify.get_scopes()
    spotify.auth_code = input("Enter Code: ")
    spotify.perform_auth()
