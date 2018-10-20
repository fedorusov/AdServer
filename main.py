from PyQt5 import QtCore, QtGui, QtWidgets
from wrapped_gui import W_Ui_MainWindow
import sys

def main():

    pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    W_ui = W_Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
