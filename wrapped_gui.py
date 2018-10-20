from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class W_Ui_MainWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ad server"))
        self.ui.checkBox.toggled['bool'].connect(self.betaLInput_handler)
        self.ui.checkBox.toggled['bool'].connect(self.ui.betaRInput.setEnabled)
        self.ui.checkBox.toggled['bool'].connect(self.ui.betaStep.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def betaLInput_handler(self, is_enabled):
        if is_enabled:
            self.ui.betaLInput.setPlaceholderText("Left border")
        else:
            self.ui.betaLInput.setPlaceholderText("")