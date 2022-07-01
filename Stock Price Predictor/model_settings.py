# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from settings_applied import *
from invalid_settings import *
import sqlite3, os.path, sys
from dataScraper import createDB, connectDB

lasso_settings = {
    'max_iter': 1000,
    'alpha': 0.1,
    'tol': 0.0017
}

enet_settings = {
    'max_iter': 1000,
    'alpha': 0.1,
    'tol': 0.0017,
    'l1_ratio': 0.7
}

model_selection = ['Lasso']

class Ui_Model_Settings(object): 
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 206)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(2, "")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def defaultSettings(self):
        conn = connectDB()
        cursor = conn.cursor() 
        cursor.execute("""DELETE FROM MODEL_SETTINGS""")
        conn.commit()
        query = """INSERT INTO MODEL_SETTINGS (Model, max_iter, alpha, tol) VALUES (?, ?, ?, ?)"""
        default_lasso = ('Lasso', int(1000), float(0.1), float(0.0017))
        try:
            cursor.execute(query, default_lasso)
        except:
            createDB()
            cursor.execute(query, default_lasso)
        conn.commit()
        query = """INSERT INTO MODEL_SETTINGS (Model, max_iter, alpha, tol, l1_ratio) VALUES (?, ?, ?, ?, ?)"""
        default_enet = ('ElasticNet', int(1000), float(0.1), float(0.0017), float(0.7))
        cursor.execute(query, default_enet)
        conn.commit()
        cursor.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Model Settings"))
        self.label.setText(_translate("MainWindow", "Model:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Lasso"))
        self.comboBox.setItemText(1, _translate("MainWindow", "ElasticNet"))
        self.label_2.setText(_translate("MainWindow", "Max Iterations:"))
        self.lineEdit.setText(str(lasso_settings['max_iter']))
        self.pushButton.clicked.connect(self.apply_settings) # apply settings
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal) # Modal always on top
        self.label_3.setText(_translate("MainWindow", "Alpha:"))
        self.label_4.setText(_translate("MainWindow", "Tolerance:"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))

        conn = connectDB()
        cursor = conn.cursor() 
        if model_selection[0] == 'Lasso':
            cursor.execute("""SELECT * FROM MODEL_SETTINGS WHERE Model = 'Lasso'""")
            row = cursor.fetchone()
            self.comboBox.setCurrentText('Lasso')
            self.lineEdit.setText(str(row[1]))
            self.lineEdit_2.setText(str(row[2]))
            self.lineEdit_3.setText(str(row[3]))

        if model_selection[0] == 'ElasticNet':
            cursor.execute("""SELECT * FROM MODEL_SETTINGS WHERE Model = 'ElasticNet'""")
            row = cursor.fetchone()
            self.comboBox.setCurrentText('ElasticNet')
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setObjectName("label_5")
            self.gridLayout.addWidget(self.label_5, 4, 0 , 1, 1)
            self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
            self.lineEdit_4.setObjectName("lineEdit_4")
            self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)
            self.label_5.setText(_translate("MainWindow", "L1 Ratio"))
            self.lineEdit_4.setText(str(enet_settings['l1_ratio']))
            self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
            self.pushButton.setText(_translate("MainWindow", "Apply"))
            self.lineEdit.setText(str(row[1]))
            self.lineEdit_2.setText(str(row[2]))
            self.lineEdit_3.setText(str(row[3]))
            self.lineEdit_4.setText(str(row[4]))

        self.comboBox.currentTextChanged.connect(self.model_change) # trigger from selecting new model

    def model_change(self):
        _translate = QtCore.QCoreApplication.translate
        global model_selection
        model_selection[0] = self.comboBox.currentText() # current model selection #######
        
        conn = connectDB()
        cursor = conn.cursor() 
        if model_selection[0] == 'Lasso':
            cursor.execute("""SELECT * FROM MODEL_SETTINGS WHERE Model = 'Lasso'""")
            row = cursor.fetchone()
            self.lineEdit.setText(str(row[1]))
            self.lineEdit_2.setText(str(row[2]))
            self.lineEdit_3.setText(str(row[3]))
            self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
            if self.lineEdit_4.isVisible():
                self.lineEdit_4.deleteLater()
                self.label_5.deleteLater()
                self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
                self.pushButton.setText(_translate("MainWindow", "Apply"))
        if model_selection[0] == 'ElasticNet':
            cursor.execute("""SELECT * FROM MODEL_SETTINGS WHERE Model = 'ElasticNet'""")
            row = cursor.fetchone()
            self.lineEdit.setText(str(row[1]))
            self.lineEdit_2.setText(str(row[2]))
            self.lineEdit_3.setText(str(row[3]))
            self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setObjectName("label_5")
            self.gridLayout.addWidget(self.label_5, 4, 0 , 1, 1)
            self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
            self.lineEdit_4.setObjectName("lineEdit_4")
            self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)
            self.label_5.setText(_translate("MainWindow", "L1 Ratio"))
            self.lineEdit_4.setText(str(row[4]))
            self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 1)
            self.pushButton.setText(_translate("MainWindow", "Apply"))         

    def apply_settings(self):
        global model_selection
        model_selection[0] = self.comboBox.currentText() # current model selection #######
        
        conn = connectDB()
        cursor = conn.cursor() 
        if model_selection[0] == 'Lasso': 
            data_tuple = (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text())      
            try:
                model_selection[0] = 'Lasso'
                cursor.execute("""UPDATE MODEL_SETTINGS SET
                max_iter = ?,
                alpha = ?,
                tol = ?
                WHERE Model = 'Lasso'""", data_tuple)
                conn.commit()
                cursor.execute("""SELECT * FROM MODEL_SETTINGS WHERE Model = 'Lasso'""")
                row = cursor.fetchone()
                from sklearn.linear_model import Lasso
                Lasso(alpha=float(row[2]),
                max_iter=int(row[1]),
                tol=float(row[3]))
                self.settingsapplied()
            except:
                self.invalidSettings()

        elif model_selection[0] == 'ElasticNet':
            data_tuple = (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text())      
            try:
                model_selection[0] = 'ElasticNet'
                cursor.execute("""UPDATE MODEL_SETTINGS SET
                max_iter = ?,
                alpha = ?,
                tol = ?,
                l1_ratio = ?
                WHERE Model = 'ElasticNet'""", data_tuple)
                conn.commit()
                cursor.execute("""SELECT * FROM MODEL_SETTINGS WHERE Model = 'ElasticNet'""")
                row = cursor.fetchone()
                from sklearn.linear_model import ElasticNet
                ElasticNet(alpha=float(row[2]),
                tol=float(row[3]),
                max_iter=int(row[1]),
                l1_ratio=float(row[4]))
                self.settingsapplied()
            except:
                self.invalidSettings()

    def settingsapplied(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SettingsApplied()
        self.ui.setupUi(self.window)
        self.window.show()

    def invalidSettings(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InvalidSettings()
        self.ui.setupUi(self.window)
        self.window.show()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Model_Settings()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
