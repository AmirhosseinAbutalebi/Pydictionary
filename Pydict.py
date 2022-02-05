# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PydictUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import pandas


class Ui_MainWindow(object):

    pathCsv = "Dict.csv"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon("PydictLogo.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.resize(318, 350)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(100, 60, 110, 40))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.translatebtn)

        self.getString = QtWidgets.QTextEdit(self.centralwidget)
        self.getString.setGeometry(QtCore.QRect(30, 10, 250, 35))
        self.getString.setObjectName("getString")

        self.labelForTranslate = QtWidgets.QLabel(self.centralwidget)
        self.labelForTranslate.setGeometry(QtCore.QRect(40, 130, 245, 150))
        self.labelForTranslate.setTextFormat(QtCore.Qt.AutoText)
        self.labelForTranslate.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelForTranslate.setObjectName("labelForTranslate")

        self.labelForShowLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelForShowLogo.setGeometry(QtCore.QRect(130, 260, 61, 51))
        self.labelForShowLogo.setPixmap(QtGui.QPixmap("PydictLogo.png"))
        self.labelForShowLogo.setScaledContents(True)
        self.labelForShowLogo.setObjectName("labelForShowLogo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 318, 26))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.changeCsv)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exitProgram)

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pydict"))
        self.submitButton.setText(_translate("MainWindow", "Translate"))
        self.labelForTranslate.setText(_translate("MainWindow", ""))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def setText(self):
        string = self.getString.toPlainText()
        return string

    def changeCsv(self):
        csvFile = QFileDialog.getOpenFileName()
        splitpath = csvFile[0].split("/")
        if ".csv" in splitpath[-1]:
            self.pathCsv = csvFile[0]

    def readCsvFile(self):
        dataFrameDict = pandas.read_csv(self.pathCsv)
        return dataFrameDict

    def messageError(self):
        icon = QtGui.QIcon("PydictLogo.png")
        msg = QMessageBox()
        msg.setWindowIcon(icon)
        msg.setWindowTitle("Pydict")
        msg.setText("Word not Found.")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        e = msg.exec_()

    def translate(self, df):
        inputText = self.setText()
        try:
            for i in range(len(df)):
                if inputText in df["english"][i]:
                    indexfindword = df.index[df['english']==inputText].tolist().pop()
                    return  df["farsi"][indexfindword]
                    break
        except:
            self.messageError()


    def exitProgram(self):
        exit(0)

    def translatebtn(self):
        textShow = self.translate(self.readCsvFile())
        self.labelForTranslate.setText(textShow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
