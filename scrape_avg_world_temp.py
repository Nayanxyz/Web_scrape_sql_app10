import requests
import selectorlib
import datetime
import time

url = "https://programmer100.pythonanywhere.com/"

now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")

def temp(url):
    response = requests.get(url)
    source = response.text
    return source

def temp_extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("world_temp.yaml")
    value = extractor.extract(source)["temp"]
    return value

def store(value):
    with open("world_tempdata.txt", "a") as file:
        file.write(f"{date},{value}"+ "\n")


def read(value):
    with open("world_tempdata.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    while True:
        scraped = temp(url)
        extracted = temp_extract(scraped)
        print(extracted)
        store(extracted)
        time.sleep(900)                # every  15 mins