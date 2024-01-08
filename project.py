# -*- coding: utf-8 -*-
import subprocess
import re
import paho.mqtt.publish as publish
import time
import random
import csv
from datetime import datetime, timedelta
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload

def get_sensor_data(sensor_id):
    command = "tdtool --list-sensors | awk -F '[= \t]+' '/id={}/ {{print $10, $12}}'".format(sensor_id)
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = result.communicate()[0].decode("utf-8").strip()
    return output


mqtt_broker_address = "raspberrypi2b"
mqtt_topic = "sensor_data"
csv_file_path = "WeatherData.csv"
# sensor ID
sensor_id = 247

def publish_sensor_data():
    # get message
    sensor_data = get_sensor_data(sensor_id)

    # get value from sensors
    matches = re.findall(r'[-+]?\d*\.\d+|\d+', sensor_data)
    temperature = float(matches[0])
    humidity = int(matches[1])

    # random value for windspeed

    windspeed = round(random.uniform(0, 10), 1)


    # get current time
    current_time = datetime.now()

    # publish  MQTT
    message = "Time: {}, Temperature: {:.2f}, Humidity: {}, Windspeed: {:.2f}".format(current_time, temperature, humidity, windspeed)
    publish.single(mqtt_topic, message, hostname=mqtt_broker_address)

    print("Published:", message)

    # Execute every hour
    #if current_time.minute == 0:
        #write_to_csv(current_time, temperature, humidity, windspeed)
		
	# testing
    if  current_time.second == 0:
        write_to_csv(current_time, temperature, humidity, windspeed)


def write_to_csv(time, temperature, humidity, windspeed):
    # set second and micro second as 0
    time = time.replace(second=0, microsecond=0)

    # write csv
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # write column header
        if file.tell() == 0:
            writer.writerow(['datetime', 'temp', 'humidity', 'winspeed'])
        
        # format time
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([formatted_time, temperature, humidity, windspeed])
		
        current_time = datetime.now()
        #if current_time.minute == 0:         #Testing
        if current_time.second == 0:
            update_file('WeatherData.csv')#




SCOPES = ['https://www.googleapis.com/auth/drive.file']
SERVICE_ACCOUNT_FILE = 'Drive.json'
FOLDER_ID = '1Pa9i_Ypl1eytP-elsVlwf4CVlAbwBsZq'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)


#upload csv file to google drive
def update_file(file_path):
    try:
        file_name = os.path.basename(file_path)

        # search file 
        files = drive_service.files().list(q=f"name='{file_name}' and '{FOLDER_ID}' in parents").execute().get('files', [])

        if files:
            # there is a same name file > update
            existing_file_id = files[0]['id']
            media = MediaFileUpload(file_path, resumable=True)
            drive_service.files().update(fileId=existing_file_id, media_body=media).execute()
            print(f'File updated: {file_name}')
        else:
            # create a new file named WeatherData.csv
            file_metadata = {
                'name': file_name,
                'parents': [FOLDER_ID]
            }
            media = MediaFileUpload(file_path, resumable=True)
            new_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            print(f'File created: {new_file["id"]} ({file_name})')

    except Exception as e:
        print(f"An error occurred during file update/upload: {e}")
        



if __name__ == "__main__":
    while True:
        next_minute = datetime.now() + timedelta(minutes=1)
        next_minute = next_minute.replace(second=0, microsecond=0)

        try:
            # Waiting for the next whole minute.
            #time.sleep((next_minute - datetime.now()).total_seconds())
            
            publish_sensor_data()

        except Exception as e:
            print(f"An error occurred: {e}")
            















'''










if __name__ == "__main__":
    
    while True:
        # caculate next task date
        next_minute = datetime.now() + timedelta(minutes=1)
        next_minute = next_minute.replace(second=0, microsecond=0)

        # Waiting for the next whole minute.
        time.sleep((next_minute - datetime.now()).total_seconds())

        publish_sensor_data()
'''
