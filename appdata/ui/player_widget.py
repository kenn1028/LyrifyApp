# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PlayerWidget(object):
    def __init__(self, PlayerWidget):
        self.PlayerWidget = PlayerWidget
    #def setupUi(self, PlayerWidget):
        PlayerWidget.setObjectName("PlayerWidget")
        PlayerWidget.setEnabled(True)
        PlayerWidget.resize(450, 150)
        PlayerWidget.setMinimumSize(QtCore.QSize(450, 0))
        PlayerWidget.setMaximumSize(QtCore.QSize(450, 150))
        PlayerWidget.setGeometry(QtCore.QRect(0, 0, 450, 150))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        PlayerWidget.setFont(font)
        PlayerWidget.setAutoFillBackground(False)
        PlayerWidget.setStyleSheet("QWidget {\n"
"    background-color: rgb(24, 24, 24);\n"
"}")
        self.song_progressBar = QtWidgets.QProgressBar(PlayerWidget)
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
        self.user_profile = QtWidgets.QPushButton(PlayerWidget)
        self.user_profile.setGeometry(QtCore.QRect(410, 0, 40, 40))
        self.user_profile.setStyleSheet("QPushButton{\n"
"    background-color: rgb(24, 24, 24);\n"
"    color: white;\n"
"    border: none;\n"
"    shadows: none;\n"
"}")
        self.user_profile.setObjectName("user_profile")
        self.settings = QtWidgets.QToolButton(PlayerWidget)
        self.settings.setGeometry(QtCore.QRect(410, 40, 40, 40))
        self.settings.setStyleSheet("QToolButton{\n"
"    background-color: rgb(24, 24, 24);\n"
"    color: white;\n"
"    border: none;\n"
"    shadows: none;\n"
"}")
        self.settings.setObjectName("settings")
        self.song_name = QtWidgets.QLabel(PlayerWidget)
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
        self.label = QtWidgets.QLabel(PlayerWidget)
        self.label.setGeometry(QtCore.QRect(170, 70, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: rgb(179, 179, 179);\n"
"}")
        self.label.setObjectName("label")
        self.song_image = QtWidgets.QFrame(PlayerWidget)
        self.song_image.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.song_image.setAutoFillBackground(False)
        self.song_image.setStyleSheet("QFrame{\n"
"    background-color: rgb(154, 154, 154);\n"
"}")
        self.song_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.song_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_image.setObjectName("song_image")
        self.song_progress = QtWidgets.QLabel(PlayerWidget)
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
        self.song_length = QtWidgets.QLabel(PlayerWidget)
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

        self.retranslateUi(PlayerWidget)
        QtCore.QMetaObject.connectSlotsByName(PlayerWidget)

    def retranslateUi(self, PlayerWidget):
        _translate = QtCore.QCoreApplication.translate
        PlayerWidget.setWindowTitle(_translate("PlayerWidget", "Form"))
        self.user_profile.setText(_translate("PlayerWidget", "Profile"))
        self.settings.setText(_translate("PlayerWidget", "..."))
        self.song_name.setText(_translate("PlayerWidget", "song_name"))
        self.label.setText(_translate("PlayerWidget", "artist_name"))
        self.song_progress.setText(_translate("PlayerWidget", "0:24"))
        self.song_length.setText(_translate("PlayerWidget", "3:20"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlayerWidget = QtWidgets.QWidget()
    ui = Ui_PlayerWidget()
    ui.setupUi(PlayerWidget)
    PlayerWidget.show()
    sys.exit(app.exec_())
