# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from settings_applied import Ui_SettingsApplied

lasso_settings = {
    'default_iter': 1000,
    'alpha': 0.1,
    'tol': 0.0017
}

#default_iter = 1000

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

    def retranslateUi(self, MainWindow):
        global lasso_settings
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Model:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Lasso"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Test"))
        self.label_2.setText(_translate("MainWindow", "Max Iterations:"))
        self.lineEdit.setText(str(lasso_settings['default_iter']))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.pushButton.clicked.connect(self.apply_settings) # apply settings
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal) # Modal always on top
        self.label_3.setText(_translate("MainWindow", "Alpha:"))
        self.label_4.setText(_translate("MainWindow", "Tolerance:"))
        self.pushButton.setText(_translate("MainWindow", "Done"))
        self.lineEdit.setText(str(lasso_settings['default_iter']))
        self.lineEdit_2.setText(str(lasso_settings['alpha']))
        self.lineEdit_3.setText(str(lasso_settings['tol']))
        self.comboBox.currentTextChanged.connect(self.model_change) # selecting new model

    def model_change(self, MainWindow):
        model_selection = self.comboBox.currentText() # current model selection #######
        if model_selection == 'Lasso':
            #self.alphaUi(MainWindow)
            print('Lasso UI')
        if model_selection == 'Test':
            print('Change UI!!!@@@')
    
    def apply_settings(self):
        model_selection = self.comboBox.currentText() # current model selection #######
        if model_selection == 'Lasso':        
            global lasso_settings
            lasso_settings['default_iter'] = self.lineEdit.text()
            lasso_settings['alpha'] = self.lineEdit_2.text()
            lasso_settings['tol'] = self.lineEdit_3.text()
            self.settingsapplied()
        if model_selection == 'Test':
            print('Nothing Changed')

        #print(self.comboBox.currentText()) # read combobox selection
        #self.alphaUi(MainWindow) # change model ui
        
    def alphaUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label_3.setText(_translate("MainWindow", "Alpha:"))
        self.pushButton.setText(_translate("MainWindow", "Done"))

    def settingsapplied(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SettingsApplied()
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
