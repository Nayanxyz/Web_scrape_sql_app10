import requests
import selectorlib
import datetime
import sqlite3
import time

url = "https://programmer100.pythonanywhere.com/"



connection = sqlite3.connect("world_temp.db")

def temp(url):
    response = requests.get(url)
    source = response.text
    return source

def temp_extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("../world_temp.yaml")
    value = extractor.extract(source)["temp"]
    return value

def store(extracted):
    now = datetime.datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%H:%M:%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO tempdatasql VALUES(?, ?, ?)", (date, time, extracted))
    connection.commit()

if __name__ == "__main__":
    while True:
        scraped = temp(url)
        extracted = temp_extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(5)