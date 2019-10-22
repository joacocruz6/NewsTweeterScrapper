import psycopg2
import sys
import csv
from variables import USERNAME,PASSWORD
from uploader import HOST,DBNAME,PORT,DATA_PATH;

def main(args: list)->int:
    try:
        connection = psycopg2.connect(
            user=USERNAME,password=PASSWORD,host=HOST,port=PORT,database=DBNAME)
        cursor = connection.cursor()
        query = "SELECT * FROM scrapper.tweets"
        cursor.execute(query)
        records = cursor.fetchall()
        with open('exports.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in records:
                writer.writerow(row)
    except(Exception,psycopg2.Error) as error:
        print("Error while fetching data",error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Postgres connection closed")
        return 0
if __name__ == "__main__":
    main(sys.argv)