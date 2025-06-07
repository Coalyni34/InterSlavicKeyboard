import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from alphavets import keyboardController

if __name__ == "__main__":
    controller = keyboardController.controllerKeyboard()
    controller.start()   