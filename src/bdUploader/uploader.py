import json
import psycopg2
import sys
from variables import USERNAME, PASSWORD
HOST = "127.0.0.1"  # localhost
DBNAME = "postgres"
PORT = "5432"
DATA_PATH = '../jsonData/'


def main(args: list) -> int:
    jfile = DATA_PATH + args[1]
    try:
        connection = psycopg2.connect(
            user=USERNAME, password=PASSWORD, host=HOST, port=PORT, database=DBNAME)
        cursor = connection.cursor()
        with open(jfile, 'r') as read_data:
            raw_data = json.load(read_data)
            for data in raw_data:
                query = """INSERT INTO scrapper.tweets ("tweet_id","user",hour,tweet_text) VALUES (%s,%s,%s,%s)"""
                record_to_insert = (data['user'], data['date'], data['text'])
                cursor.execute(query, record_to_insert)
                connection.commit()
                count = cursor.rowcount
                print(count, "Record inserted into the table")
    except (Exception, psycopg2.Error) as error:
        print("Error while connection to Postgres", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Postgres connection closed")
        return 0


if __name__ == "__main__":
    main(sys.argv)
