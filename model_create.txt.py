import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import time
import os
import datetime
import IPython
import IPython.display
import matplotlib as mpl
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Input
from sklearn.metrics import confusion_matrix
from google.colab import drive


drive.mount('/content/gdrive')
df_weather = pd.read_csv('gdrive/MyDrive/model/weatherHistory.csv')


df_weather.info()

df_weather[20: 400:24]

print ("Unique values are:\n",df_weather.nunique())

df_weather = df_weather.sort_values(by='Formatted Date')
df_weather[20: 400:24]


wt_missing = df_weather.isna().sum()
wt_missing

missing_value_count = (df_weather.isnull().sum())
print(missing_value_count[missing_value_count > 0])
total_cells = np.product(df_weather.shape)
total_missing_value = missing_value_count.sum()
print("Total percentage of our missing value is:",round((total_missing_value / total_cells * 100),4))
print('Total number of our cells is :',total_cells)
print('Total number of our missing value is :',total_missing_value)


df_weather['Precip Type'].fillna(df_weather['Precip Type'].value_counts().index[0],inplace=True)
df_weather.isna().sum()

df_weather.drop(["Daily Summary"], axis=1, inplace=True)
df_weather.columns

df_weather['Loud Cover'].value_counts()
df_weather.drop(['Loud Cover'],axis=1,inplace=True)


df_weather.columns

Summary_Weather=df_weather["Summary"].value_counts().reset_index()
Summary_Weather.columns=["Weather Type","Count"]
Summary_Weather

print(df_weather['Summary'].unique())

df_weather = pd.get_dummies(df_weather, columns = ['Summary'])
print(df_weather)


precip_Label= df_weather["Precip Type"].value_counts().reset_index()
precip_Label.columns=["Precip Type","Count"]
precip_Label


le = LabelEncoder()
df_weather['Precip Type']=le.fit_transform(df_weather['Precip Type'])
df_weather.head(10)


Data visualization
date_time = pd.to_datetime(df_weather.pop('Formatted Date'), format='%Y-%m-%d %H:%M:%S.%f %z')
plot_cols = df_weather.columns
plot_features = df_weather[plot_cols]
plot_features.index = date_time
plot_features.plot( figsize=(20,35), subplots=True)



df_weather.describe().transpose()
df_weather["Pressure (millibars)"].value_counts()






































