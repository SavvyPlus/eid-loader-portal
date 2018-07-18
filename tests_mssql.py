import os

import pymssql
from dotenv import load_dotenv

load_dotenv()


SERVER = os.getenv("SERVER")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")


conn = pymssql.connect(SERVER, USERNAME, PASSWORD, DATABASE)

cursor = conn.cursor()

cursor.execute('SELECT * FROM RawEDI LIMIT 88')
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()
