import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import bs4

class HumidityPlot():
   # def draw(self):
        df_weather = pd.read_csv('weatherHistory.csv')
        df_weather = df_weather.sort_values(by='Formatted Date')
        df_weather['date_time'] = pd.to_datetime(df_weather.pop('Formatted Date'), format='%Y-%m-%d %H:%M:%S.%f %z')

        fig = px.line(df_weather, x='date_time', y='Humidity', title='Humidity over Time')
        fig.update_xaxes(rangeslider_visible=True)  # Add a range slider for zooming in time
        # html_plot = pio.to_html(fig, full_html=False)
        fig.show()
        # fig.write_html('humidity_plot.html')
        #
        # # Print the file path or URL
        # print('File saved as: humidity_plot.html')