from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from function_class import GenFunction, Function
import graphics

def num_check(*variables):
    """
    Checking if numeric variables are valid
    """
    return variables + (True, )

class W_Ui_MainWindow(Ui_MainWindow):
    def __init__(self, MainWindow):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.is_auto = False
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ad server"))
        self.ui.checkBox.toggled['bool'].connect(self.betaLInput_handler)
        self.ui.checkBox.toggled['bool'].connect(self.ui.betaRInput.setEnabled)
        self.ui.checkBox.toggled['bool'].connect(self.ui.betaStep.setEnabled)
        self.ui.calculateButton.clicked.connect(self.calculate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def betaLInput_handler(self, is_enabled):
        if is_enabled:
            self.ui.betaLInput.setPlaceholderText("Left border")
        else:
            self.ui.betaLInput.setPlaceholderText("")
        self.is_auto = is_enabled

    def parse(self):
        self.p, p_corr = GenFunction(['w'], self.ui.distInput.text())
        self.S, S_corr = GenFunction(['t'], self.ui.planInput.text())
        self.f, f_corr = GenFunction(['z', 'x', 'S', 'b'], self.ui.corrInput.text())
        self.betaL, self.betaR, self.betaS, beta_corr = num_check(self.ui.betaLInput.text(), self.ui.betaRInput.text(), self.ui.betaStep.text())
        self.z, z_corr = GenFunction(['t'], self.ui.trafInput.text())
        self.x0, self.y0, start_corr = num_check(self.ui.X0Input.text(), self.ui.Y0Input.text())
        if not p_corr or not S_corr or not f_corr or not beta_corr or not z_corr or not start_corr:
            self.error()

    def calculate(self):
        self.parse()

        print('calculated!')

        graphics.show_results()

    def error(self):
        pass
