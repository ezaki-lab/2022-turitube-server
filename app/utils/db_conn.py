import pymysql.cursors
import os
from .config import config

print(config)
HOSTNAME = config["ftp"]["hostname"]
USER = config["ftp"]["user"]
PASSWORD = config["ftp"]["password"]
DB = config["ftp"]["db"]


def sql_connection(text):
    conn = pymysql.connect(host = HOSTNAME,
                             user = USER,
                             password = PASSWORD,
                             db = DB,
                             charset='utf8',
                             # 結果の受け取り方の指定。Dict形式で結果を受け取ることができる
                             cursorclass=pymysql.cursors.DictCursor)

    with conn.cursor(pymysql.cursors.DictCursor) as cur:
        cur.execute(text)
        data = cur.fetchall()
        conn.commit()
        return data

if __name__ == "__main__":
    print(sql_connection("""SELECT * FROM `User` WHERE 1"""))