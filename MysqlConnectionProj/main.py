import os, pygame

from mysql.connector import connection, connect


def main():
    conn = connect(user='user', password='pass', host='localhost', database='example')
    cursor1 = conn.cursor()

    try:
        cursor1.execute("drop table testing")
        conn.commit()

    finally:
        cursor1.close()

    conn.close()


if __name__ == '__main__':
    main()


@staticmethod
class TestClass:
    def __init__(self):
        self.x = 2
