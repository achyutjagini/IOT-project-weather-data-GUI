from PyQt5.QtWidgets import QApplication
# from GUI2 import main_window
# from GUI_trial import main_window2
from PyQt5.uic import loadUi
import GUI2
import GUI_trial

if __name__ == "__main__":
    app = QApplication([])

    window1 = GUI2.MainWindow()
    window2 = GUI_trial.MainWindow2()

    window1.window2 = window2
    window2.window1 = window1

    window1.show()
    app.exec_()
