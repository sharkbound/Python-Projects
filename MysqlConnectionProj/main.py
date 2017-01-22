import os

from mysql.connector import connection, connect


def main():
    conn = connect(user='user', password='pass', host='localhost', database='example')
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()

    try:
        cursor1.execute("drop table testing")
        conn.commit()


    finally:
        cursor1.close()


    conn.close()


if __name__ == '__main__':
    main()
