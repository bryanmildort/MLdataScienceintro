# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_History(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionClear_History = QtWidgets.QAction(MainWindow)
        self.actionClear_History.setObjectName("actionClear_History")
        self.actionClear_History.triggered.connect(self.clear_history)  
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_History)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_initial_data()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prediction History"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionClear_History.setText(_translate("MainWindow", "Clear History"))
    
    def clear_history(self):
        import sqlite3, os.path, sys
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "history.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM RESULTS""")
        conn.commit()
        cursor.close()
        
        self.load_initial_data()
        #self.setupUi(MainWindow)


    def load_initial_data(self):
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["Date", "Time", "Ticker", "High", "Low", "Close", "Model", "R2"])
        self.tableWidget.setColumnWidth(0, 110)
        self.tableWidget.setColumnWidth(1, 85)
        self.tableWidget.setColumnWidth(2, 67)
        self.tableWidget.setColumnWidth(3, 160)
        self.tableWidget.setColumnWidth(4, 160)
        self.tableWidget.setColumnWidth(5, 160)
        self.tableWidget.setColumnWidth(6, 320)
        self.tableWidget.setColumnWidth(7, 160)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        import sqlite3, os.path
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "history.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM RESULTS''')
        rows = cursor.fetchall()

        for row in rows:
            inx = rows.index(row)
            self.tableWidget.insertRow(inx)
            # add more if there is more columns in the database.
            self.tableWidget.setHorizontalHeaderLabels(["Date", "Time", "Ticker", "High", "Low", "Close"])
            self.tableWidget.setItem(inx, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(inx, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(inx, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(inx, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(inx, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(inx, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(inx, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableWidget.setItem(inx, 7, QtWidgets.QTableWidgetItem(str(row[7])))