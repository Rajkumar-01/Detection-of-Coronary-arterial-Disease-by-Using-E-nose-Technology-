import requests
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


CHANNEL_ID = "2499099"
READ_API_KEY = "Z0LV0SYBNJEXBI98"

def fetch_data(channel_id, read_api_key):

    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_api_key}&results=15"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['feeds']
    else:
        print("Failed to fetch data")
        return []

def plot_fields_1_and_2(data):
    """Plot the data for fields 1 and 2."""
    timestamps = [datetime.strptime(feed['created_at'], '%Y-%m-%dT%H:%M:%SZ') for feed in data]
    field1_values = [float(feed['field1']) if feed['field1'] else None for feed in data]
    field2_values = [float(feed['field3']) if feed['field3'] else None for feed in data]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, field1_values, marker='o', label='ACETONE')
    plt.plot(timestamps, field2_values, marker='s', label='TOLUENE')

    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('ACETONE and TOLUENE')
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate() # Rotation
    plt.tight_layout()
    plt.show()

def plot_field_3(data):
    timestamps = [datetime.strptime(feed['created_at'], '%Y-%m-%dT%H:%M:%SZ') for feed in data]
    field3_values = [float(feed['field2']) if feed['field2'] else None for feed in data]

    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, field3_values, marker='^', label='BENZENE', color='green')

    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('BENZENE')
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate() # Rotation
    plt.tight_layout()
    plt.show()

# Fetch the data
data = fetch_data(CHANNEL_ID, READ_API_KEY)
if data:
    plot_fields_1_and_2(data)
    plot_field_3(data)
