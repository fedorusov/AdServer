from PyQt5 import QtCore, QtGui, QtWidgets
from wrapped_gui import Gui
import sys

def main():
    #test
    pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Gui = Gui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
