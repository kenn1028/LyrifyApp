# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lyrics_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LyricsWidget(object):
    def __init__(self, LyricsWidget):
        self.LyricsWidget = LyricsWidget

    #def setupUi(self, LyricsWidget):
        LyricsWidget.setObjectName("LyricsWidget")
        LyricsWidget.resize(450, 450)
        LyricsWidget.setStyleSheet("QWidget{\n"
"    background: rgb(40, 40, 40)\n"
"}")
        self.textEdit = QtWidgets.QTextEdit(LyricsWidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 450, 415))
        font = QtGui.QFont()
        font.setKerning(True)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    background: rgb(40, 40, 40);\n"
"    border: 1px solid rgb(35, 35, 35);\n"
"}")
        self.textEdit.setLineWidth(0)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.textEdit.setTabChangesFocus(False)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setObjectName("textEdit")
        self.nativeButton = QtWidgets.QPushButton(LyricsWidget)
        self.nativeButton.setGeometry(QtCore.QRect(0, 415, 150, 35))
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
"    shadows: none;\n"
"}")
        self.nativeButton.setObjectName("nativeButton")
        self.romanjiButton = QtWidgets.QPushButton(LyricsWidget)
        self.romanjiButton.setGeometry(QtCore.QRect(150, 415, 150, 35))
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
"    shadows: none;\n"
"}")
        self.romanjiButton.setObjectName("romanjiButton")
        self.engishButton = QtWidgets.QPushButton(LyricsWidget)
        self.engishButton.setGeometry(QtCore.QRect(300, 415, 150, 35))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova Rg")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.engishButton.setFont(font)
        self.engishButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(40, 40, 40);\n"
"    color: white;\n"
"    border: none;\n"
"    shadows: none;\n"
"}")
        self.engishButton.setObjectName("engishButton")

        self.retranslateUi(LyricsWidget)
        QtCore.QMetaObject.connectSlotsByName(LyricsWidget)

    def retranslateUi(self, LyricsWidget):
        _translate = QtCore.QCoreApplication.translate
        LyricsWidget.setWindowTitle(_translate("LyricsWidget", "Form"))
        self.textEdit.setHtml(_translate("LyricsWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PLACE NATIVE LYRICS HERE</p></body></html>"))
        self.nativeButton.setText(_translate("LyricsWidget", "Native"))
        self.romanjiButton.setText(_translate("LyricsWidget", "Romanized"))
        self.engishButton.setText(_translate("LyricsWidget", "English"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LyricsWidget = QtWidgets.QWidget()
    ui = Ui_LyricsWidget()
    ui.setupUi(LyricsWidget)
    LyricsWidget.show()
    sys.exit(app.exec_())
