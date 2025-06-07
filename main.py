import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from graphics import mainwindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()

    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(window)
    window.show()

    sys.exit(app.exec_())