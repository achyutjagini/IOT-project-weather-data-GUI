import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import MDS

from matplotlib.colors import ListedColormap

data = pd.read_csv("beach_weather_station_no_missing_values.csv")
data.head(10)
data.info()
data2 =pd.read_csv("Stockholm,Sweden 2022-07-01 to 2023-11-25.csv")
