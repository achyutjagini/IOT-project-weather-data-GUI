from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome
import os
from PyQt5.QtWebKitWidgets import QGraphicsWebView
from PyQt5.QtWidgets import QWidget
from gnewsclient import gnewsclient
import webbrowser
import hum_draw
from plotly.offline import plot

class MainUi(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # creat main part
        self.main_layout = QtWidgets.QGridLayout()  # creat layout
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget()  # creat left part
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()   # creat layout
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QtWidgets.QWidget()  # create right part
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # Set main part

        self.left_close = QtWidgets.QPushButton("")  # close botton
        self.left_visit = QtWidgets.QPushButton("")  # space button
        self.left_mini = QtWidgets.QPushButton("")  # min button

        self.left_label_1 = QtWidgets.QPushButton("Daily news")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("App functions")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("@Yihang")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.database', color='white'), "Historical data")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.cloud', color='white'), "Weather analysis")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.map', color='white'), "Local map")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.headphones', color='white'), "Follow US")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.phone', color='white'), "Report BUGs")
        self.left_button_5.setObjectName('left_button')


        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 7, 0, 1, 3)

        self.draw_widget = QtWidgets.QWidget()
        self.draw_widget.setObjectName("right_widget2")
        self.draw_layout = QtWidgets.QGridLayout()
        self.draw_widget.setLayout(self.draw_layout)

        self.humidity_label = QtWidgets.QPushButton("Show hitorical")
        self.humidity_label.setObjectName('right_label')

        current_dir = os.path.dirname(os.path.realpath(__file__))
        html_file_path = os.path.join(current_dir, 'humidity_plot.html')
        self.web_view = QGraphicsWebView()
        self.web_view.setObjectName('plotshow')
        self.web_view.setHtml(html_file_path)
        self.web_view_container = QWidget.createWindowContainer(self.web_view)


        self.right_layout.addWidget(self.draw_widget,1,2,11,10)
        self.right_layout.addWidget(self.humidity_label,0,2,1,1)
        self.draw_layout.addWidget(self.web_view_container,1,2,11,10)
        ##  QSS
        self.left_close.setFixedSize(30, 30)  # set size
        self.left_visit.setFixedSize(30, 30)  # set size
        self.left_mini.setFixedSize(30, 30)  # set size

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
                    QPushButton{border:none;color:white;}
                    QPushButton#left_label{
                        border:none;
                        border-bottom:1px solid white;
                        font-size:18px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                    QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
                ''')




def main():
            app = QtWidgets.QApplication(sys.argv)
            gui = MainUi()
            gui.show()
            sys.exit(app.exec_())

if __name__ == '__main__':
            main()