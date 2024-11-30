import pandas as pd
from utils.mysql_connect import mysql_connect


def fetch_weather_records():
    connection = mysql_connect()
    if connection.is_connected():
        cursor = connection.cursor()
        query = "SELECT * FROM weather_records"

        cursor.execute(query)
        rows = cursor.fetchall()
        # columns = ["a","b","c"]

        # df = pd.DataFrame(rows, columns)

        print(rows)

        connection.close()

fetch_weather_records()