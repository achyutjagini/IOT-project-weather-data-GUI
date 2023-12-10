from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtCore import QObject, pyqtSlot
import GUI_trial1

##GUI_trial






##GUI2
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.ui.m_c_b.clicked.connect(self.switch2page2)

    @pyqtSlot()
    def switch2page2(self):
        loadUi('GUI_trial.ui', self)
if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()