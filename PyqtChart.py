import sys
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

class DataGenerator:
    def __init__(self, callback):
        self.callback = callback
        self.timer = QTimer()
        self.timer.timeout.connect(self.generate_data)
        self.timer.start(1000)  # 1000ms = 1 second

    def generate_data(self):
        data = random.randint(10, 30)
        self.callback(data)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Chart")
        self.setGeometry(100, 100, 800, 600)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.fig)
        self.setCentralWidget(self.canvas)

        self.x_data = []
        self.y_data = []

        self.data_generator = DataGenerator(self.update_chart)

    def update_chart(self, data):
        self.x_data.append(time.strftime("%H:%M:%S"))
        self.y_data.append(data)

        if len(self.x_data) > 6:
            self.x_data = self.x_data[-6:]
            self.y_data = self.y_data[-6:]

        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data)
        self.ax.set_ylim(0, 40)
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())









