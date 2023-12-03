#from sklearn.impute import SimpleImputer
#from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA
#from sklearn.manifold import MDS
#from matplotlib.colors import ListedColormap
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.model_selection import train_test_split
#from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
from tkinter import Toplevel
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt



# Function to plot the data
def plot_data(filepath):
    data = pd.read_csv(filepath,index_col=0)
    date_time = pd.to_datetime(data['Measurement Timestamp'].copy(), format='%m/%d/%Y %I:%M:%S %p')
    plot_cols = [col for col in data.columns if col != 'Measurement Timestamp']
    plot_features = data[plot_cols]
    plot_features.index = date_time
    plot_features.plot(figsize=(20, 35), subplots=True)
    plt.show()

# Function called when Historical Data Visualization button is clicked
def load_and_plot():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        plot_data(filepath)

# Function to display the saved plot
def display_saved_plot(image_path):
    plot_window = Toplevel(root)
    plot_window.title("LSTM predictions")

    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)

    img_label = tk.Label(plot_window, image=img)
    img_label.image = img
    img_label.pack()

# Set up the Tkinter GUI
root = tk.Tk()
root.title("IoT Weather Data Application")
window_width = 800  # Width of the window
window_height = 600  # Height of the window

# Get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find the center position
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# Add a button for Historical Data Visualization
visualization_button = tk.Button(root, text="Historical Data Visualization", command=load_and_plot)
visualization_button.pack(pady=10)  # Add vertical padding for spacing

# Add a button for Historical Data LSTM Prediction
lstm_prediction_button = tk.Button(root, text="Historical Data LSTM Prediction", command=lambda: display_saved_plot('air_temperature_comparison.png'))
lstm_prediction_button.pack(pady=10)  # Add vertical padding for spacing

# Start the GUI event loop
root.mainloop()
