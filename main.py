import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

url = "http://programmer100.pythonanywhere.com/tours/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:                                                                  # functions become methods in classes
    def scrape(self, url):
        """ scrape the page source from url """
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source

    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value

class Email:
    def send(seld, message):
        host = "smtp.gmail.com"
        port = 465

        username = "nayan7857@gmail.com"
        password = "jguieilgubjxffsg"

        receiver = "nayanxyz0@gmail.com"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("email is sent")

class Database:
    """ __init__ is a special method and is automatically called every time a new instance (object) of the class is created.
        You do not call __init__ explicitly. Python handles this automatically when you instantiate a class.

        self is a reference to the current instance (object) of the class, allowing you to access its
        attributes and methods from within the class definition.
        self links the methods and attributes defined within the class to the specific object that is calling the method.

      """

    def __init__(self, database_path):
        self.connection = sqlite3.connect(database_path)          # class contain args in __init__ method like data_path = data.db


    def store(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        cursor = connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
        connection.commit()

    def read(self, extracted):
        row = extracted.split(",")
        row = [item.strip() for item in row]
        band, city, date = row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
        rows = cursor.fetchall()
        print(rows)
        return rows

if __name__ == "__main__":
    while True:
        event = Event()
        scraped = event.scrape(url)
        extracted = event.extract(scraped)
        print(extracted)

        if extracted != "No upcoming tours":
            database = Database(database_path="data.db")   # class gets argument
            row = database.read(extracted)
            if not row:
                database.store(extracted)
                email = Email()
                email.send(message="Hey, new event is found")
            time.sleep(2)