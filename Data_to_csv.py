import csv
from datetime import datetime
import time
import random
import os

def get_sensor_data():
    #simulation
    temperature = random.randint(20, 35)
    humidity = random.randint(20, 35)
    return  temperature, humidity


def save_to_csv(data):
    filename = f"sensor_data_{datetime.now().strftime('%Y%m%d%H')}.csv"
    header = ["Timestamp", "Temperature (°C)", "Humidity (%)"]

    # create file if file does not exist
    if not os.path.isfile(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

    # save data in file
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    while True:
        try:
            temperature, humidity = get_sensor_data()

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            #set second = 0
            #current_time = datetime.now().replace(second=0).strftime('%Y-%m-%d %H:%M:%S')

            print(f"{current_time} - Temperature: {temperature}°C, Humidity: {humidity}%")

            # save
            save_to_csv([current_time, temperature, humidity])

            # wait for next o'clock
            #time.sleep(3600 - time.time() % 3600)

            time.sleep(2)

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

