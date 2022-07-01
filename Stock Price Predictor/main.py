# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from predictions import Ui_Predictions
from history import Ui_History
from model_settings import *
from about import *
from predictor import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(303, 264)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionSettings.triggered.connect(self.modelSettings) # open model settings
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.aboutWindow)
        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")
        self.actionHistory.triggered.connect(self.openHistory)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionHistory)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.pushButton.clicked.connect(self.predict) # adding function to Predict! button
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def predict(self): # predict function, LEARN ABOOUT CLASSES@@@
        global ticker
        ticker = self.lineEdit.text()
        predict_end = predictor(ticker)
        if predict_end == None:
            return
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Predictions()
        self.ui.setupUi(self.window)
        self.window.show()

    def modelSettings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Model_Settings()                
        self.ui.setupUi(self.window)
        self.window.show()

    def aboutWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_About()                
        self.ui.setupUi(self.window)
        self.window.show()

    def openHistory(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_History()                
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Price Predictor"))
        self.label.setText(_translate("MainWindow", "Enter Ticker To Scrape:"))
        self.pushButton.setText(_translate("MainWindow", "Predict!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Model Settings"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHistory.setText(_translate("MainWindow", "History"))
        Ui_Model_Settings.defaultSettings(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
