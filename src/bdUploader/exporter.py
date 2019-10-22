import psycopg2
import sys
import csv
from variables import USERNAME,PASSWORD
from uploader import HOST,DBNAME,PORT,DATA_PATH;

def main(args: list)->int:
    try:
        table = args[1]
        table_type = args[2]
        connection = psycopg2.connect(
            user=USERNAME,password=PASSWORD,host=HOST,port=PORT,database=DBNAME)
        cursor = connection.cursor()
        query = f"SELECT * FROM scrapper.{table}"
        cursor.execute(query)
        records = cursor.fetchall()
        with open(f'exports_{table_type}.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["tweet_id","twitter_user","hour","tweet_text"])
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