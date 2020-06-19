'''
Spotify Lyrics Player Project (June 2020)

Dependencies:
pip install pyqt5
pip install pyqt5-tools


Opening Qt Designer in console: type: "pyqt5designer"

PS.
ElectronJS : https://www.electronjs.org/docs/tutorial/first-app#installing-electron
            https://www.youtube.com/watch?v=627VBkAhKTc
Xojo : https://www.xojo.com/?utm_source=quora&utm_medium=content&utm_campaign=dev
'''
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from spotify_client import SpotifyAPI
from lyrics_scraper import ColorCodedLyrics

class PyQT_UI(QMainWindow):
    def __init__(self):
        super(PyQT_UI, self).__init__()
        self.setGeometry(1200, 250, 450, 600)
        self.setWindowTitle("LyrifyApp")
        self.initUI()

        wid = playerWidget()

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(wid,0,0)
        self.frame.setLayout(self.grid)

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Play")
        self.b1.move(200, 200)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("WEEWOOOOOOOOOWO")
        self.update()

    def update(self):
        self.label.adjustSize()

class playerWidget(QtWidgets.QWidget):
    def __init__(self):
        #QtWidgets.QWidget.__init__(self)
        super(playerWidget, self).__init__()
        uic.loadUi("player_widget.ui", self)
        self.show()

def window():
    app = QApplication(sys.argv)
    win = PyQT_UI()

    win.show()
    sys.exit(app.exec_())

####-----int main()-----####

spotify = SpotifyAPI()
lyrics = ColorCodedLyrics(song_name = "Airplane", artist_name = "IZONE")

window()

dict = lyrics.get_lyrics()

with open('lyrics.txt', 'w', encoding = "utf-8") as w:
    for n in dict:
        w.write(dict[n])

# spotify.get_scopes()
# spotify.auth_code = input("Enter Code: ")
# spotify.perform_auth()
