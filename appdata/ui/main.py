# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.player_widget = Ui_PlayerWidget(self.centralwidget)
        self.player_widget.setGeometry(QtCore.QRect(0, 0, 450, 150))
        self.player_widget.setMinimumSize(QtCore.QSize(450, 150))
        self.player_widget.setMaximumSize(QtCore.QSize(450, 150))
        self.player_widget.setToolTip("")
        self.player_widget.setWhatsThis("")
        self.player_widget.setStyleSheet("")
        self.player_widget.setObjectName("player_widget")
        self.lyrics_widget = Ui_LyricsWidget(self.centralwidget)
        self.lyrics_widget.setGeometry(QtCore.QRect(0, 150, 450, 450))
        self.lyrics_widget.setObjectName("lyrics_widget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

from lyrics_widget import Ui_LyricsWidget
from player_widget import Ui_PlayerWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
