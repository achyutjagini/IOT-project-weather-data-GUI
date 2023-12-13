import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Specify the path to your local HTML file
        html_file_path = 'file:///Users/yihangqiao/Documents/GitHub/IOT-project-weather-data-GUI/GUI/humidity_plot.html'

        self.webview = QWebEngineView()

        try:
            # Load the local HTML file using QUrl.fromLocalFile
            self.webview.setUrl(QUrl.fromLocalFile(html_file_path))
        except Exception as e:
            print(f"Error loading HTML file: {e}")

        self.setCentralWidget(self.webview)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec_())
