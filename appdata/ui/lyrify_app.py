'''
Spotify Lyrics Player Project (June 2020)

Dependencies:
pip install pyqt5
pip install pyqt5-tools


Opening Qt Designer in console: type: "pyqt5designer"
Converting .ui to .py: type: 'pyuic5 -x file.ui -o file.py'

PS.
ElectronJS : https://www.electronjs.org/docs/tutorial/first-app#installing-electron
            https://www.youtube.com/watch?v=627VBkAhKTc
Xojo : https://www.xojo.com/?utm_source=quora&utm_medium=content&utm_campaign=dev
'''

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
from threading import Thread
import sys
import time
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from main_gui import UpdateThread
from spotify_client import SpotifyAPI
from lyrics_scraper import ColorCodedLyrics
# import worker

#  ========================================================================================== #

'''
Notes:
> change thread approach, avoid doing .request on update functions
> reduce # of requests
> lyrics fetching not separated in the thread



A.) QThread
    1.) Make new thread:
        while True:
            get_current_song
            if ui song name != song name

                Options:
                    a.) .write() data into temp .txt (?)
                    b.)

                signal.emit(update_ui)

B.) Python Threading
    1.) Make new thread:
        while True:
            constantly checks and writes current_song data and lyrics on a temp .txt

    2.) UI function reads off the temp .txt file
            can use pyqtsignal to check for file updates so it doesn't need to check everytime

    3.) Progress bar
            using QThread might be the easiest way, or can also use pyqtsignal to read off the temp .txt file


Features to be added (according to priority):

> PyQtDesigner Changes
    1.) Window size
    - Resizable or fixed
    2.)

> Toggle language buttons

> Profile picture button, and redirect to Spotify URL
    - needs get_profile() functions in SpotifyAPI Class

> App logo for main bar and taskbar

> Aesthetics Changes
    1.) Lyrics scroll bar - minimalist, flat
    2.) Window bar -  hide/recolor
    3.) Lyrics - font style and size
    4.) Add Green accent on buttons/UI

> Settings button
    - Light mode (?)

'''

#  ========================================================================================== #

class Ui_MainWindow(object):
    # MainWindow = QtWidgets.QMainWindow()
    data = None
    song_name_ = None
    artist_name_ = None
    song_length_ = None
    song_progress_ = None
    lyrics = None

    def __init__(self):
        super().__init__()

        self.obj = UpdateThread()
        self.thread = QThread()

        self.obj.signal.connect(self.update_player)

        self.obj.moveToThread(self.thread)

        self.obj.finished.connect(self.thread.quit)

        self.thread.started.connect(self.obj.update)
        # self.thread.started.connect(self.obj.update)

        self.thread.start()

    # def startThread(self):
    #     self.myThread = UpdateThread()
    #     self.myThread.signal.connect(self.update_player)
    #     self.myThread.start()

    # def __init__(self):
    #     super().__init__()
    #
    #     # 1 - create Worker and Thread inside the Form
    #     self.obj = worker.Worker()  # no parent!
    #     self.thread = QThread()  # no parent!
    #
    #     # 2 - Connect Worker`s Signals to Form method slots to post data.
    #     self.obj.song_update.connect(self.onIntReady)
    #
    #     # 3 - Move the Worker object to the Thread object
    #     self.obj.moveToThread(self.thread)
    #
    #     # 4 - Connect Worker Signals to the Thread slots
    #     self.obj.finished.connect(self.thread.quit)
    #
    #     # 5 - Connect Thread started signal to Worker operational slot method
    #     self.thread.started.connect(self.obj.update)
    #
    #     # * - Thread finished signal will close the app if you want!
    #     #self.thread.finished.connect(app.exit)
    #
    #     # 6 - Start the thread
    #     self.thread.start()
    #
    #     # 7 - Start the form
    #     self.setupUi(QtWidgets.QMainWindow())
    #     # QtWidgets.QMainWindow().show()
    #
    # def onIntReady(self, i):
    #     song_name = i
    #     if self.song_name_ != song_name:
    #         self.update_player()
    #     #print(i)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        MainWindow.setStyleSheet("QMainWindow {\n"
            "    background-color: rgb(24, 24, 24);\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
            "    background-color: rgb(40, 40, 40);\n"
            "}")
        self.centralwidget.setObjectName("centralwidget")
        self.player_widget = QtWidgets.QWidget(self.centralwidget)
        self.player_widget.setGeometry(QtCore.QRect(0, 0, 450, 150))
        self.player_widget.setStyleSheet("QWidget {\n"
            "    background-color: rgb(24, 24, 24);\n"
            "}")
        self.player_widget.setObjectName("player_widget")
        self.song_image = QtWidgets.QWidget(self.player_widget)
        self.song_image.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.song_image.setAutoFillBackground(False)
        self.song_image.setStyleSheet("QFrame{\n"
            "    background-color: rgb(154, 154, 154);\n"
            "}")
        self.song_image.setObjectName("song_image")
        self.label_3 = QtWidgets.QLabel(self.song_image)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("song_cover.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.player_widget)
        self.label.setGeometry(QtCore.QRect(170, 70, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
            "    color: rgb(179, 179, 179);\n"
            "}")
        self.label.setObjectName("label")
        self.song_length = QtWidgets.QLabel(self.player_widget)
        self.song_length.setGeometry(QtCore.QRect(365, 120, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.song_length.setFont(font)
        self.song_length.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.song_length.setStyleSheet("QLabel{\n"
            "    color: rgb(179, 179, 179);\n"
            "}")
        self.song_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.song_length.setObjectName("song_length")
        self.song_progress = QtWidgets.QLabel(self.player_widget)
        self.song_progress.setGeometry(QtCore.QRect(170, 120, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.song_progress.setFont(font)
        self.song_progress.setStyleSheet("QLabel{\n"
            "    color: rgb(179, 179, 179);\n"
            "}\n"
            "")
        self.song_progress.setObjectName("song_progress")
        self.user_profile = QtWidgets.QPushButton(self.player_widget)
        self.user_profile.setGeometry(QtCore.QRect(410, 0, 40, 40))
        self.user_profile.setMouseTracking(True)
        self.user_profile.setStyleSheet("QPushButton{\n"
            "    background-color: rgb(24, 24, 24);\n"
            "    color: white;\n"
            "    border: none;\n"
            "}\n"
            " QPushButton:pressed {\n"
            "    background-color: rgb(20, 20, 20);     \n"
            "    color: white;\n"
            "    border: none;\n"
            " }\n"
            " QPushButton:hover {\n"
            "    background-color: rgb(60, 60, 60);\n"
            "    color: white;\n"
            "    border: none;\n"
            " }")
        self.user_profile.setObjectName("user_profile")
        self.settings = QtWidgets.QToolButton(self.player_widget)
        self.settings.setGeometry(QtCore.QRect(410, 40, 40, 40))
        self.settings.setStyleSheet("QToolButton{\n"
            "    background-color: rgb(24, 24, 24);\n"
            "    color: white;\n"
            "    border: none;\n"
            "}\n"
            " QToolButton:pressed {\n"
            "    background-color: rgb(20, 20, 20);     \n"
            "    color: white;\n"
            "    border: none;\n"
            " }\n"
            " QToolButton:hover {\n"
            "    background-color: rgb(60, 60, 60);\n"
            "    color: white;\n"
            "    border: none;\n"
            " }")
        self.settings.setObjectName("settings")
        self.song_name = QtWidgets.QLabel(self.player_widget)
        self.song_name.setGeometry(QtCore.QRect(170, 40, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Alt Rg")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.song_name.setFont(font)
        self.song_name.setStyleSheet("QLabel{\n"
            "    color: white;\n"
            "}")
        self.song_name.setOpenExternalLinks(True)
        self.song_name.setObjectName("song_name")
        self.song_progressBar = QtWidgets.QProgressBar(self.player_widget)
        self.song_progressBar.setGeometry(QtCore.QRect(170, 110, 250, 6))
        self.song_progressBar.setStyleSheet("QProgressBar:horizontal {\n"
            "border-radius: 2px;\n"
            "background: rgb(64, 64, 64);\n"
            "}\n"
            "QProgressBar::chunk:horizontal {\n"
            "border-radius: 2px;\n"
            "background: rgb(179, 179, 179);\n"
            "}")
        self.song_progressBar.setProperty("value", 24)
        self.song_progressBar.setTextVisible(False)
        self.song_progressBar.setObjectName("song_progressBar")


        self.lyrics_widget = QtWidgets.QWidget(self.centralwidget)
        self.lyrics_widget.setGeometry(QtCore.QRect(0, 150, 450, 450))
        self.lyrics_widget.setObjectName("lyrics_widget")
        self.nativeButton = QtWidgets.QPushButton(self.lyrics_widget)
        self.nativeButton.setGeometry(QtCore.QRect(0, 410, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nativeButton.setFont(font)
        self.nativeButton.setStyleSheet("QPushButton{\n"
            "    background-color: rgb(35, 35, 35);\n"
            "    color: white;\n"
            "    border: none;\n"
            "}")
        self.nativeButton.setObjectName("nativeButton")
        self.pushButton = QtWidgets.QPushButton(self.lyrics_widget)
        self.pushButton.setGeometry(QtCore.QRect(300, 410, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
            "    background-color: rgb(40, 40, 40);\n"
            "    color: white;\n"
            "    border: none;\n"
            "}")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.lyrics_widget)
        self.textEdit.setGeometry(QtCore.QRect(0, -5, 450, 415))
        font = QtGui.QFont()
        font.setKerning(True)
        self.textEdit.setFont(font)
        self.textEdit.setMouseTracking(False)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("QTextEdit{\n"
            "    background: rgb(40, 40, 40);\n"
            "    border: 1px solid rgb(35, 35, 35);\n"
            "}")
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(0)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setObjectName("textEdit")
        self.romanjiButton = QtWidgets.QPushButton(self.lyrics_widget)
        self.romanjiButton.setGeometry(QtCore.QRect(150, 410, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.romanjiButton.setFont(font)
        self.romanjiButton.setStyleSheet("QPushButton{\n"
            "    background-color: rgb(40, 40, 40);\n"
            "    color: white;\n"
            "    border: none;\n"
            "}")
        self.romanjiButton.setObjectName("romanjiButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.startThread()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LyrifyApp"))
        self.label.setText(_translate("MainWindow", "artist_name"))
        self.song_length.setText(_translate("MainWindow", "song_length"))
        self.song_progress.setText(_translate("MainWindow", "song_progress"))
        self.user_profile.setText(_translate("MainWindow", "Profile"))
        self.settings.setText(_translate("MainWindow", "..."))
        self.song_name.setText(_translate("MainWindow", "song_name"))
        self.nativeButton.setText(_translate("MainWindow", "Native"))
        self.pushButton.setText(_translate("MainWindow", "English"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.romanjiButton.setText(_translate("MainWindow", "Romanized"))

    def update_player(self):
        _translate = QtCore.QCoreApplication.translate

        data = spotify.get_current_song()
        song_name = data["title"]
        artist_name = data["artist"]
        song_length = data["song_length"]

        self.label.setText(f"{artist_name}")
        self.song_length.setText(f"{song_length}")
        self.song_name.setText(f"{song_name}")
        self.label_3.setPixmap(QtGui.QPixmap("song_cover.png"))

        if self.song_name_ != song_name:
            lyrics = ColorCodedLyrics(song_name = song_name, artist_name = artist_name).get_lyrics()
            self.lyrics = str(lyrics["native"])
            self.lyrics = self.lyrics.replace('<td>', '').replace('</td>', '')

            self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
            f"<div class='centeralign'><span align=\"center\" style=\" color: '#c7c7c7'; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><center><br>{self.lyrics}<br></center></span></div></body></html>"))

            self.song_name_ = song_name
            time.sleep(1)

        # value = int((float(song_progress.replace(':', '.'))/float(song_length.replace(':', '.'))) * 100)
        # ui.song_progress.setText(f"{song_progress}")
        # ui.song_progressBar.setProperty("value", value)

    def update_progress(self):
        data = spotify.get_current_song_progress()
        song_length = data["song_length"]
        song_progress = data["song_progress"]
        value = int((float(song_progress.replace(':', '.'))/float(song_length.replace(':', '.'))) * 100)
        self.song_progress.setText(f"{song_progress}")
        self.song_progressBar.setProperty("value", value)

class UpdateThread(QObject):
    signal = pyqtSignal()
    finished = pyqtSignal()

    @pyqtSlot()
    def update(self):
        while True:
            data = spotify.get_current_song_progress()
            song_name = data["title"]

            if ui.song_name_ != song_name:
                self.signal.emit()
                time.sleep(1)

            self.finished.emit()
            time.sleep(1)

#  ========================================================================================== #

# class Worker(QObject):
#     finished = pyqtSignal()
#     song_update = pyqtSignal(str)
#     ui = Ui_MainWindow()
#
#     @pyqtSlot()
#     def update(self):
#         while True:
#             data = spotify.get_current_song_progress()
#             # print(data)
#             song_name = data["title"]
#
#             if ui.song_name_ != song_name:
#                 self.song_update.emit(song_name)
#                 self.finished.emit()
#
#     # def procCounter(self): # A slot takes no params
#     #     for i in range(1, 100):
#     #         time.sleep(1)
#     #         self.intReady.emit(i)
#     #
#     #     self.finished.emit()

#  ========================================================================================== #

spotify = SpotifyAPI()

try:
    spotify.perform_refresh()
except:
    spotify.get_scopes()
    spotify.auth_code = input("Enter Code: ")
    spotify.perform_auth()

# if __name__ == "__main__":
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
# ui.startThread()
# ui.myThread.start()
# timer = QtCore.QTimer()
# timer.timeout.connect(ui.update_progress)
# timer.start(1100)
sys.exit(app.exec_())
