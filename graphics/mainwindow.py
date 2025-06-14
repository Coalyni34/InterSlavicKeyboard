import json
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from alphavets import jsonReader, symbolsController
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(268, 156)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("inter.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Prefiks_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.Prefiks_lineedit.setGeometry(QtCore.QRect(50, 30, 81, 16))
        self.Prefiks_lineedit.setObjectName("Prefiks_lineedit")
        self.Keyboard_label = QtWidgets.QLabel(self.centralwidget)
        self.Keyboard_label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.Keyboard_label.setFont(font)
        self.Keyboard_label.setObjectName("Keyboard_label")
        self.Switch_label = QtWidgets.QLabel(self.centralwidget)
        self.Switch_label.setGeometry(QtCore.QRect(10, 50, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.Switch_label.setFont(font)
        self.Switch_label.setObjectName("Switch_label")
        self.Switch_programm_chekbox = QtWidgets.QCheckBox(self.centralwidget)
        self.Switch_programm_chekbox.setGeometry(QtCore.QRect(10, 70, 211, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Switch_programm_chekbox.setFont(font)
        self.Switch_programm_chekbox.setObjectName("Switch_programm_chekbox")
        self.Ok_button = QtWidgets.QPushButton(self.centralwidget)
        self.Ok_button.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.Ok_button.setObjectName("Ok_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 90, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 268, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Ok_button.clicked.connect(lambda: self.onpress_okbutton(   self.Switch_programm_chekbox.isChecked(),
                                                                        self.Prefiks_lineedit.text()
                                                                        ))
        
        if os.path.exists("settings.json"):
            with open('settings.json', 'r', encoding='utf-8') as f:
                loaded_settings = json.load(f)
            self.Prefiks_lineedit.setText(loaded_settings["Prefiks"])
            self.Switch_programm_chekbox.setChecked(loaded_settings["isActive"])
            self.setupKeyboardController()
        else:
            _reader = jsonReader.jsonReaderClass()
            _reader.saveSettings(True, '\\')
            with open('settings.json', 'r', encoding='utf-8') as f:
                loaded_settings = json.load(f)
            self.Prefiks_lineedit.setText(loaded_settings["Prefiks"])
            self.Switch_programm_chekbox.setChecked(loaded_settings["isActive"])
            self.setupKeyboardController()
    
    def onpress_okbutton(self, isActive, prefiks):   
        _reader = jsonReader.jsonReaderClass()
        _reader.saveSettings(isActive, prefiks)
        QApplication.quit()
    
    def setupKeyboardController(self):
        controller = symbolsController.controllerKeyboard(self.Prefiks_lineedit.text())
        if self.Switch_programm_chekbox.isChecked():
            controller.start()
            print(self.Switch_programm_chekbox.isChecked())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Interslavic Keyboard"))
        self.Keyboard_label.setText(_translate("MainWindow", "Tipkovnica \\ Типковница"))
        self.Switch_label.setText(_translate("MainWindow", "Prěključati \\ Прєкључати"))
        self.Switch_programm_chekbox.setText(_translate("MainWindow", "Programa aktivny \\ Програма актвины"))
        self.Ok_button.setText(_translate("MainWindow", "ОК"))
        self.label.setText(_translate("MainWindow", "Prefiks:"))
        self.label_2.setText(_translate("MainWindow", "(Perezaładujte program)"))
