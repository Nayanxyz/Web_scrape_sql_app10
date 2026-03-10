import sqlite3                                                      # SQLite3 is a widely used, serverless, lightweight, and
                                                                    # file-based SQL database engine built into Python, Android, and many other applications.
                                                                    # It requires no configuration, making it ideal for prototyping, internal application storage,
                                                                    # or small-to-medium datasets

# establish a connection and a cursor
connection = sqlite3.connect("data.db")                            # The sqlite3.connect() function in Python is used to establish a connection to an SQLite database file.
                                                                   # If the specified database file does not exist, it will be automatically created. This function returns
                                                                   # a Connection object used to interact with the database

cursor = connection.cursor()                                       # The connection.cursor() method is used to create a cursor object, which acts as an intermediary for executing
                                                                   # SQL queries and managing results within a database session. The connection object itself manages the connection
                                                                   # to the database, while the cursor object handles the specific commands and data retrieval

# Query all data based on condition("*" is for all)
cursor.execute("SELECT * FROM events WHERE band ='Lion'")          #In Python database programming, the cursor.execute() method is used to send and run a SQL query or command against
                                                                   # the database. It serves as the primary mechanism for interacting with the database through a cursor object.
rows = cursor.fetchall()
print(rows)

cursor.execute("SELECT * FROM events WHERE date ='2026.12.11'")
rows = cursor.fetchall()
print(rows)

# Query certain column
cursor.execute("SELECT band, date FROM events WHERE date ='2026.12.11'")           #
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'cat city', '2026.12.12'),('Bats', 'bat city', '2026.12.12') ]

                              #??? is three rows, band,city..
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)                   #The cursor.executemany() method in Python's database API is used to execute a single
                                                                                       # SQL operation (like INSERT, UPDATE, or DELETE) multiple times with a sequence of different parameters.

connection.commit()                                                                    #The connection.commit() method is used in database programming to permanently save all changes made
                                                                                       # within the current transaction to the database

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)