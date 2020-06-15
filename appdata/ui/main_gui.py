from PyQt5 import QtCore, QtGui, QtWidgets
from spotify_client import SpotifyAPI
from lyrics_scraper import ColorCodedLyrics
from threading import Thread
from ui_MainWindow import Ui_MainWindow

import sys
import time

if __name__ == '__main__':
    def update_player():
        _translate = QtCore.QCoreApplication.translate

        data = spotify.get_current_song()
        song_name = data["title"]
        artist_name = data["artist"]
        song_length = data["song_length"]
        song_progress = data["song_progress"]

        lyrics = ColorCodedLyrics(song_name = song_name, artist_name = artist_name).get_lyrics()
        lyrics = lyrics["native"]

        value = int((float(song_progress.replace(':', '.'))/float(song_length.replace(':', '.'))) * 100)

        ui.label.setText(f"{artist_name}")
        ui.song_length.setText(f"{song_length}")
        ui.song_progress.setText(f"{song_progress}")
        ui.song_name.setText(f"{song_name}")
        ui.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        f"<div class='centeralign'><p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">{lyrics}</p></div></body></html>"))
        ui.label_3.setPixmap(QtGui.QPixmap("song_cover.png"))
        ui.song_progressBar.setProperty("value", value)
        time.sleep(1)

    spotify = SpotifyAPI()

    spotify.get_scopes()
    spotify.auth_code = input("Enter Code: ")
    spotify.perform_auth()
    lyrics = None

    data = None
    song_name = None
    artist_name = None
    song_length = None
    song_progress = None

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # window = MainWindow()
    # window.show()
    # app = QtGui.QApplication(sys.argv)

    timer = QtCore.QTimer()
    timer.timeout.connect(update_player)
    timer.start(1000)

    # data = spotify.get_current_song()
    # song_name = data["title"]
    # artist_name = data["artist"]
    # song_length = data["song_length"]
    # song_progress = data["song_progress"]


    sys.exit(app.exec_())
