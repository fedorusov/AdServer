import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import sys

def main():
    pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())